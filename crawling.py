from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from psutil import virtual_memory
import pandas as pd
import multiprocessing
import pyautogui
import datetime
import time


def convert_date(item_date):
    item_date = item_date.replace("년 ", "-").replace("월 ", "-").replace("일", "")
    item_date = datetime.datetime.strptime(item_date, "%Y-%m-%d").date()
    return item_date


def merge_review(item_L_review, item_review):
    if item_review == '' and item_L_review != '':
        return item_L_review
    else:
        return item_review


if __name__ == '__main__':
    url = "https://play.google.com/store/apps/details?id=com.yantech.orient.tojung&hl=ko&showAllReviews=true"
    url2 = "https://play.google.com/store/apps/details?id=com.ipapas.sajulite&hl=ko&showAllReviews=true"
    url3 = "https://play.google.com/store/apps/details?id=com.un7qi3.forceteller&hl=ko&showAllReviews=true"
    url4 = "https://play.google.com/store/apps/details?id=com.thingsflow.hellobot&hl=ko&showAllReviews=true"
    url5 = "https://play.google.com/store/apps/details?id=handasoft.mobile.divination&hl=ko&showAllReviews=true"

    tstart_time = time.time()
    driverPath = "D:\\shin2no\\chromedriver.exe"
    driver = webdriver.Chrome(driverPath)
    driver.get(url)
    pyautogui.keyDown('win')
    pyautogui.press('right', presses=2, interval=0.2)
    pyautogui.keyUp('win')
    pyautogui.press('enter')

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
            print(">>>>>> \t last_height : %d \t new_height : %d \t memory_usage : %.1f%%" % (
            last_height, new_height, memory_usage))
            last_height = new_height
        #elif new_height > 80000:
         #   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          #  break
        elif memory_usage > 86.9 or new_height > 3000000:  # 크롬 메모리 부족으로 인한 종료 방지
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print(">>> \t The usage of system memory exceeds 90%, stopping crawling.")
            break
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print(">>> \t last_height : %d \t new_height : %d \t memory_usage : %.1f%%" % (
                last_height, new_height, memory_usage))
            last_height = new_height
    time.sleep(5)

    # 장문 리뷰 전체 리뷰 버튼 일괄 클릭 동작
    spread_review = driver.find_elements_by_xpath("//button[@jsaction='click:TiglPc']")
    for i in range(len(spread_review)):
        if spread_review[i].is_displayed():
            driver.execute_script("arguments[0].click();", spread_review[i])  # 클릭 대상이 가려져 execute_script()를 사용해야함
            time.sleep(0.5)
            print(">>> \t (%d/%d)th review button is clicked..." % ((i + 1), len(spread_review)))
    print("******** finished << all_review button >> clicking ********")
    time.sleep(5)

    # 크롤링
    num_cores = multiprocessing.cpu_count()

    start_time = time.time()
    L_reviews = [element.text for element in driver.find_elements_by_xpath("//span[@jsname='fbQN7e']")]
    T_reviews = [[element.text, element] for element in driver.find_elements_by_xpath("//span[@class='IEFhEe']")]
    print("******** finished << L/T_review : %s, %s >> crawling ********" % (len(L_reviews), str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0]))

    start_time = time.time()
    reviews = [element.text for element in driver.find_elements_by_xpath("//span[@jsname='bN97Pc']")]
    print("******** finished << review : %s >> crawling ********" % str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

    start_time = time.time()
    for xpath in T_reviews:
        xpath[1] = driver.execute_script("gPt=function(c){if(c.id!==''){return'id(\"'+c.id+'\")'}if(c===document.body){return c.tagName}var a=0;var e=c.parentNode.childNodes;for(var b=0;b<e.length;b++){var d=e[b];if(d===c){return gPt(c.parentNode)+'/'+c.tagName+'['+(a+1)+']'}if(d.nodeType===1&&d.tagName===c.tagName){a++}}};return gPt(arguments[0]).toLowerCase();", xpath[1])
        xpath[1] = int(''.join(filter(str.isdigit, xpath[1].split('/')[-5])))
        reviews[xpath[1]-1] = xpath[0] + " " + reviews[xpath[1]-1]
    pool = multiprocessing.Pool(num_cores)
    reviews = pool.starmap(merge_review, zip(L_reviews, reviews))
    pool.close()
    pool.join()
    print("******** finished << join review : %s >> crawling ********" %
          str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

    start_time = time.time()
    dates = [element.text for element in driver.find_elements_by_xpath("//div[@class='bAhLNe kx8XBd']/div/span[@class='p2TkOb']")]
    pool = multiprocessing.Pool(num_cores)
    dates = pool.map(convert_date, dates)
    pool.close()
    pool.join()
    print("******** finished << date : %s >> crawling and replace ********" %
          str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

    start_time = time.time()
    likes = [element.text for element in driver.find_elements_by_xpath("//div[@aria-label='이 리뷰가 유용하다는 평가를 받은 횟수입니다.']")]
    print("******** finished << like : %s >> crawling ********" %
          str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

    start_time = time.time()
    stars = [element.get_attribute('aria-label')[10:11] for element in driver.find_elements_by_xpath("//span[@class='nt2C1d']/div[@class='pf5lIe']/div[@role='img']")]
    print("******** finished << star : %s >> crawling ********" %
          str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

    # 데이터 통합
    start_time = time.time()
    results = list(zip(dates, stars, likes, reviews))
    print("******** finished << review merge : %s >> ********" %
          str(datetime.timedelta(seconds=time.time() - start_time)).split(".")[0])

    # csv 저장
    data = pd.DataFrame(results, dtype='object')
    data.columns = ['날짜', '평점', '동의', '리뷰']
    pkg_name = url.split('?id=')[-1].split('&')[0]
    date_format = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H-%M-%S")
    file_name = pkg_name + "_" + date_format
    data.to_csv('D:\\google_review\\{}.csv'.format(file_name), encoding='utf-8-sig')
    print(str(datetime.timedelta(seconds=time.time() - tstart_time)).split(".")[0])
    driver.quit()
