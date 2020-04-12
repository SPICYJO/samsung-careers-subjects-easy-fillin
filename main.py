from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
import csv

from func import *
from settings import *



## Initialize
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(r".\chromedriver", options=chrome_options)
driver.implicitly_wait(3)


## 삼성채용 홈페이지

# 로그인 페이지
driver.get("https://www.samsungcareers.com/rec/apply/ComResumeServlet")
driver.find_element_by_id("email").send_keys(LOGIN_INFOs["email"])
driver.find_element_by_id("password").send_keys(LOGIN_INFOs["password"])
driver.find_element_by_xpath("//*[@id='budiv_mySheet_comLogin']/a").click()
# 로그인 알림창 닫기
wait = WebDriverWait(driver, 2);
wait.until(ExpectedConditions.alert_is_present());
alert = Alert(driver)
alert.accept()

# 지원 페이지
driver.get(applyURL)
driver.find_element_by_xpath("//*[@id='masTable1']/tr/td[3]/a").click()
# 지원서 알림창 닫기
alert = Alert(driver)
alert.accept()

# 이수교과목으로 이동
driver.find_element_by_xpath("//*[@id='cont']/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/ul/li[3]/a").click()
# 이동 알림창 닫기
Alert(driver).accept()

## CSV 읽어오기
SUBJECT_list = []
with open(r".\data.csv", 'r') as f:
    rdr = csv.reader(f)
    infoline = next(rdr)
    for line in rdr:
        SUBJECT = dict(zip(infoline, line))
        SUBJECT_list.append(SUBJECT)
    f.close()    

## 데이터 채우기
for SUBJECT in SUBJECT_list:
    add_subject(driver, SUBJECT)

    # 10회 입력창 확인
    try:
        alert = Alert(driver)
        alert.accept()
    except Exception as exc:
        pass

## 무조건 exception 발생
raise Exception("Completed")

## 종료
driver.close()
driver.quit()

## 클리어하기
# clear_subjects(driver)
