from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import time


def remove_popup():
    for handle in driver.window_handles:
        if handle != driver.window_handles[0]:
            driver.switch_to.window(handle)
            driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.frame("mainFrame")  # 프레임을 사용한 경우 해당 프레임으로 전환
    return


if __name__ == '__main__':
    url = "http://www.childcare.go.kr"
    driverPath = "D:\\shin2no\\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("lang=ko_KR")
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    driver = webdriver.Chrome(driverPath)
    driver.maximize_window()        #크롬창 최대화
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    remove_popup()

    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "로그인"))).click()
    wait.until(ec.element_to_be_clickable((By.ID, "mbrid"))).send_keys("giselle81")
    driver.find_element_by_id("uspass").send_keys("dksthdgml2@")
    driver.find_element_by_xpath("//p[@class='text_c']/input[@alt='아이디 로그인']").click()

    while 1:
        time.sleep(0.3)
        if len(driver.window_handles) > 1:
            remove_popup()
            break

    wait.until(ec.element_to_be_clickable((By.ID, "menu4"))).click()
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "입소대기"))).click()
    wait.until(ec.element_to_be_clickable((By.ID, "link_dep2_p1_040203000000"))).click()
    wait.until(ec.element_to_be_clickable((By.ID, "ctprvn")))
    Select(driver.find_element_by_id("ctprvn")).select_by_value('11000')
    # xpath using ("//select[@name='element_name']/option[text()='option_text']").click()
    time.sleep(0.1)
    Select(driver.find_element_by_id("signgu")).select_by_value('11500')
    Select(driver.find_element_by_id("crtype")).select_by_value('0101')
    target_loc = "마곡9 "
    target_loc2 = "마곡1 하람"   #테스트 코드
    driver.find_element_by_id("crname").send_keys(target_loc)
    driver.find_element_by_link_text("검색").click()

    no_search = "검색된 데이터가 없습니다."
    target_time = datetime(2021, 1, 5, 14, 31, 59)  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<edit
    ii = datetime(2021, 1, 5, 14, 31, 39)  # 테스트 코드
    i = 0       #테스트 코드

    if driver.find_element_by_xpath("//*[@id='divprint']/div/table/tbody/tr/td").text != no_search:
        target_time = datetime.now()
        print("지정된 시간 전에 목록이 활성화 되었습니다.")
    else:
        print("지정된 시간까지 대기 합니다.")

    while 1:
        now_time = datetime.now()
        if now_time > target_time and driver.find_element_by_xpath("//*[@id='divprint']/div/table/tbody/tr/td").text != no_search:
            break
        if now_time > ii and i == 0:     #테스트 코드
            driver.find_element_by_id("crname").clear()
            driver.find_element_by_id("crname").send_keys(target_loc2)
            i += 1
        if now_time > target_time:
            driver.find_element_by_link_text("검색").click()
        time.sleep(0.4)

    start_time = datetime.now()
    parent_element = driver.find_element_by_xpath("//*[contains(text(), '{0}')]".format(target_loc2))     #<<<<<edit
    parent_element.find_element_by_xpath("../../td[last()]/span/a[text()='선택']").click()
    Alert(driver).accept()      # 팝업 종료(수락)

    wait.until(ec.new_window_is_opened(driver.window_handles))
    driver.switch_to.window(driver.window_handles[-1])
    wait.until(ec.element_to_be_clickable((By.ID, "btnStipulation"))).click()
    Alert(driver).accept()

    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.frame("mainFrame")
    wait.until(ec.element_to_be_clickable((By.XPATH, "//td[last()]/input[contains(@id, '161129')]"))).click()
    driver.switch_to.window(driver.window_handles[-1])
    wait.until(ec.element_to_be_clickable((By.XPATH, "//span/input[@name='foodallrgyyn' and @value='N']"))).click()
    driver.find_element_by_xpath("//span/input[@name='indvdlinfocolctyn' and @value='Y']").click()
    driver.find_element_by_xpath("//span/input[@name='thptyprovdagreyn' and @value='Y']").click()
    driver.find_element_by_xpath("//span/input[@name='indvdlinfoprovdyn' and @value='Y']").click()
    driver.find_element_by_name("agrParentWrite").click()
    Alert(driver).accept()
    Alert(driver).accept()

    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.frame("mainFrame")
    wait.until(ec.element_to_be_clickable((By.ID, "st01"))).click()
    driver.find_element_by_id("chk2").click()
    driver.find_element_by_id("rentyn").click()
    Alert(driver).accept()
    driver.find_element_by_xpath("//div/span/a[text()='입소대기신청']").click()
    Alert(driver).accept()
    Alert(driver).accept()
    Alert(driver).accept()
    end_time = datetime.now()
    print(end_time-start_time)
    wait.until(ec.element_to_be_clickable((By.ID, "sCHILINNB2"))).click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3600)
    driver.quit()
