from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from psutil import virtual_memory
import pandas as pd
import numpy as np
import time
import datetime

tstart_time = time.time()
# url = "https://play.google.com/store/apps/details?id=com.ipapas.sajulite&hl=ko&showAllReviews=true"
#url = "https://play.google.com/store/apps/details?id=com.thingsflow.hellobot&hl=ko&showAllReviews=true"
url = "https://play.google.com/store/apps/details?id=handasoft.mobile.divination&hl=ko&showAllReviews=true"
#url = "https://play.google.com/store/apps/details?id=com.yantech.orient.tojung&hl=ko&showAllReviews=true"
#url = "https://play.google.com/store/apps/details?id=com.un7qi3.forceteller&hl=ko&showAllReviews=true"
driverPath = "D:\\shin2no\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.get(url)

# 리뷰 최하위까지 스크롤 및 더보기 버튼 클릭
wait = WebDriverWait(driver, 180)
driver.find_element_by_xpath("//div[@class='ry3kXd Ulgu9']/div[@class='MocG8c UFSXYb LMgvRb KKjvXb']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//div[@class='OA0qNb ncFHed']/div[@data-value='2']").click()
time.sleep(0.5)
new_height = 0
last_height = driver.execute_script("return document.body.scrollHeight")
print(">>> \t last_height : %d \t new_height : %d" % (new_height, last_height))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while 1:
    wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@jsname='lYU69']/div[@class='Fx1lse']")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    new_height = driver.execute_script("return document.body.scrollHeight")
    memory_usage = virtual_memory()[2]

    if new_height == last_height:
        if driver.find_elements_by_xpath("//span[@class='RveJvd snByac']"):
            driver.execute_script("arguments[0].click();",
                                  driver.find_element_by_xpath("//span[@class='RveJvd snByac']"))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            for i in range(3):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height != last_height:
                    break
                print(">>>>>> \t %d th last height checking and wait 2secs..." % (i + 1))
            if new_height == last_height and not driver.find_elements_by_xpath("//span[@class='RveJvd snByac']"):
                print("******** finished <<page scrawling>> ********")
                break
            else:
                print(">>>>>> \t last_height : %d \t new_height : %d \t memory_usage : %.1f%%" % (
                    last_height, new_height, memory_usage))
                last_height = new_height
    # elif new_height > 100000:
    #    break
    elif memory_usage > 89.9 or new_height > 3000000:  # 메모리 부족으로 인한 종료 방지
        print(">>> \t The usage of system memory exceeds 90%, stopping crawling.")
        break
    else:
        print(">>> \t last_height : %d \t new_height : %d \t memory_usage : %.1f%%" % (
            last_height, new_height, memory_usage))
        last_height = new_height

# 장문 리뷰 전체 리뷰 버튼 일괄 클릭 동작
spread_review = driver.find_elements_by_xpath("//button[@jsaction='click:TiglPc']")
for i in range(len(spread_review)):
    if spread_review[i].is_displayed():
        driver.execute_script("arguments[0].click();", spread_review[i])  # 클릭 대상이 가려져 execute_script()를 사용해야함
        time.sleep(0.5)
        print(">>> \t (%d/%d)th review button is clicked..." % ((i + 1), len(spread_review)))
print("******** finished <<all review button>> clicking ********")


# 크롤링

start_time = time.time()
t_cnt = len(driver.find_elements_by_xpath("//span[@class='IEFhEe']"))
np_T_reviews = np.empty(t_cnt, dtype='object')
for i, element in enumerate(driver.find_elements_by_xpath("//span[@class='IEFhEe']")):
    np_T_reviews[i] = element.text
print("******** finished <<T_review >> crawling ********")

r_cnt = len(driver.find_elements_by_xpath("//span[@jsname='bN97Pc']"))
np_L_reviews = np.empty(r_cnt, dtype='object')
for i, element in enumerate(driver.find_elements_by_xpath("//span[@jsname='fbQN7e']")):
    np_L_reviews[i] = element.text
print("******** finished <<L_review : %s, %s>> crawling ********" % (r_cnt, t_cnt))

ii = r_cnt - t_cnt
np_reviews = np.empty(r_cnt, dtype='object')
for i, element in enumerate(driver.find_elements_by_xpath("//span[@jsname='bN97Pc']")):
    if i >= ii:
        if element.text == '' and np_L_reviews[i] != '':
            np_reviews[i] = np_L_reviews[i]
        elif element.text == '' and np_L_reviews[i] == '':
            np_reviews[i] = np_T_reviews[i-ii]
        else:
            np_reviews[i] = element.text
    else:
        if element.text == '' and np_L_reviews[i] != '':
            np_reviews[i] = np_L_reviews[i]
        else:
            np_reviews[i] = element.text
print("******** finished <<review>> crawling ********")
print(str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

start_time = time.time()
np_dates = np.empty(r_cnt, dtype='object')
for i, element in enumerate(driver.find_elements_by_xpath("//div[@class='bAhLNe kx8XBd']/div/span[@class='p2TkOb']")):
    tmp = element.text.replace("년 ", "-").replace("월 ", "-").replace("일", "")
    np_dates[i] = datetime.datetime.strptime(tmp, "%Y-%m-%d").date()
print("******** finished <<date>> crawling and replace ********")
print(str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

np_likes = np.empty(r_cnt, dtype='object')
for i, element in enumerate(driver.find_elements_by_xpath("//div[@aria-label='이 리뷰가 유용하다는 평가를 받은 횟수입니다.']")):
    np_likes[i] = element.text
print("******** finished <<like>> crawling ********")

start_time = time.time()
np_stars = np.empty(r_cnt, dtype='object')
for i, element in enumerate(driver.find_elements_by_xpath("//span[@class='nt2C1d']/div[@class='pf5lIe']/div[@role='img']")):
    np_stars[i] = element.get_attribute('aria-label')[10:11]
print("******** finished <<star>> crawling ********")
print(str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

# 데이터 통합
start_time = time.time()
np_results = np.empty((r_cnt, 4), dtype='object')
for i in range(r_cnt):
    np_results[i][0] = np_dates[i]
    np_results[i][1] = np_stars[i]
    np_results[i][2] = np_likes[i]
    np_results[i][3] = np_reviews[i]
print("******** finished <<review merge>> ********")
print(str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

# csv 저장
data = pd.DataFrame(np_results, dtype='object')
data.columns = ['날짜', '평점', '동의', '리뷰']
pkg_name = url.split('?id=')[-1].split('&')[0]
date_format = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H-%M-%S")
file_name = pkg_name + "_" + date_format
data.to_csv('D:\\google_review\\{}.csv'.format(file_name), encoding='utf-8-sig')
print(str(datetime.timedelta(seconds=time.time() - tstart_time)).split(".")[0])
driver.quit()
