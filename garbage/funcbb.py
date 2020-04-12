from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def add_subject(driver, SUBJECT):
    driver.implicitly_wait(3)
    wait = WebDriverWait(driver, 3);
    actions = ActionChains(driver)
    
    #wait.until(ExpectedConditions.invisibility_of_element_located((By.ID, "tmp_schlcarrcdId")));

    # 과정
    elemd = driver.find_element_by_xpath('//*[@id="tmp_schlcarrcdId"]')
    actions.move_to_element(elemd).click().perform()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_schlcarrcd_List"]/ol').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text == SUBJECT["과정"]:
            webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
            break


    # 전공명
    elemd = driver.find_element_by_xpath('//*[@id="tmp_majcdId"]').click()
    webdriver.ActionChains(driver).move_to_element(elemd).click(elemd).perform()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_majcd_List"]/ol').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text == SUBJECT["전공명"]:
            webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
            break

    # 과목유형
    elemd = driver.find_element_by_xpath('//*[@id="tmp_majtypecdId"]')
    webdriver.ActionChains(driver).move_to_element(elemd).click(elemd).perform()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_majtypecd_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        tt = SUBJECT["과목유형"]
        tt = "교양기타" if tt in ("교양","일선",) else tt
        tt = "전공" if tt in ("전필","전선",) else tt
        if elem.text == tt:
            webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
            break

    # 수강년도
    elemd = driver.find_element_by_xpath('//*[@id="tmp_regyrId"]')
    webdriver.ActionChains(driver).move_to_element(elemd).click(elemd).perform()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_regyr_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text == SUBJECT["수강년도"].replace("년", ""):
            webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
            break

    # 학기
    elemd = driver.find_element_by_xpath('//*[@id="tmp_semstId"]')
    webdriver.ActionChains(driver).move_to_element(elemd).click(elemd).perform()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_semst_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text == SUBJECT["학기"].replace("1학기", "1").replace("2학기", "2").replace("여름학기", "여름계절").replace("겨울학기", "겨울계절"):
            webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
            break

    # 과목명
    driver.find_element_by_id("tmp_majcurrinm").send_keys(SUBJECT["과목명"])

    # 재수강여부
    elemd = driver.find_element_by_xpath('//*[@id="tmp_retakeynId"]')
    webdriver.ActionChains(driver).move_to_element(elemd).click(elemd).perform()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_retakeyn_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text.find(SUBJECT["재수강여부"].upper()) >= 0:
            webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
            break

    # 취득학점
    elemd = driver.find_element_by_xpath('//*[@id="tmp_obtptId"]')
    webdriver.ActionChains(driver).move_to_element(elemd).click(elemd).perform()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_obtpt_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        if elem.text.find(SUBJECT["취득학점"]) >= 0:
            webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
            break

    # 성적
    elemd = driver.find_element_by_xpath('//*[@id="tmp_obtpovId"]')
    webdriver.ActionChains(driver).move_to_element(elemd).click(elemd).perform()
    li = driver.find_element_by_xpath('//*[@id="ComboDiv_tmp_obtpov_List"]/ul').find_elements_by_tag_name('a')
    for elem in li:
        tt = SUBJECT["성적"].replace("0", "").upper()
        tt = "PASS" if tt=="S" else tt
        tt = "FAIL" if tt=="U" else tt
        if elem.text == tt:
            webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
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
            
