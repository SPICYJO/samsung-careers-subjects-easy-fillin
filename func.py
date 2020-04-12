from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.by import By
import time

## TODO: load 전 클릭하는 오류를 막기 위해 time.sleep()으로 강제대기시킴. 시간이 오래 걸린다는 단점이 있으므로 개선이 필요할 것 같음.

def add_subject(driver, SUBJECT):
    driver.implicitly_wait(3)
    wait = WebDriverWait(driver, 3);
    #wait.until(ExpectedConditions.invisibility_of_element_located((By.ID, "tmp_schlcarrcdId")));

    time.sleep(1)
    
    # 과정
    driver.find_element_by_xpath('//*[@id="tmp_schlcarrcdId"]').click()

    time.sleep(1)
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_schlcarrcd_List"]/ol').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text == SUBJECT["과정"]:
            elem.click()
            break


    time.sleep(0.5)
    # 전공명
    driver.find_element_by_xpath('//*[@id="tmp_majcdId"]').click()

    time.sleep(1)
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_majcd_List"]/ol').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text == SUBJECT["전공명"]:
            elem.click()
            break

    # 과목유형
    driver.find_element_by_xpath('//*[@id="tmp_majtypecdId"]').click()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_majtypecd_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        tt = SUBJECT["과목유형"]
        tt = "교양기타" if tt in ("교양","일선",) else tt
        tt = "전공" if tt in ("전필","전선",) else tt
        if elem.text == tt:
            elem.click()
            break

    # 수강년도
    driver.find_element_by_xpath('//*[@id="tmp_regyrId"]').click()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_regyr_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text == SUBJECT["수강년도"].replace("년", ""):
            elem.click()
            break

    # 학기
    driver.find_element_by_xpath('//*[@id="tmp_semstId"]').click()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_semst_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text == SUBJECT["학기"].replace("1학기", "1").replace("2학기", "2").replace("여름학기", "여름계절").replace("겨울학기", "겨울계절"):
            elem.click()
            break

    # 과목명
    driver.find_element_by_id("tmp_majcurrinm").send_keys(SUBJECT["과목명"])

    # 재수강여부
    driver.find_element_by_xpath('//*[@id="tmp_retakeynId"]').click()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_retakeyn_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text.find(SUBJECT["재수강여부"].upper()) >= 0:
            elem.click()
            break

    # 취득학점
    driver.find_element_by_xpath('//*[@id="tmp_obtptId"]').click()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_obtpt_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text.find(SUBJECT["취득학점"]) >= 0:
            elem.click()
            break

    # 성적
    driver.find_element_by_xpath('//*[@id="tmp_obtpovId"]').click()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_obtpov_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        tt = SUBJECT["성적"].replace("0", "").upper()
        tt = "PASS" if tt=="S" else tt
        tt = "FAIL" if tt=="U" else tt
        if elem.text == tt:
            elem.click()
            break

    # 추가하기
    driver.find_element_by_xpath('//*[@id="budiv_mySheet_AddMajdet"]/a').click()
    

def clear_subjects(driver):
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="majdetDel"]/a/img').click()
            Alert(driver).accept()
        except Exception as exc:
            break
            
