import os
import time
import config

import telegramBot
import re  # 숫자만 판별 => 남은자리 37(필답형) => 37

from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# options.add_argument("--window-size=100,100")
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get("http://www.q-net.or.kr/rcv003.do?id=rcv00301&gSite=Q&gId=")

# 시험장소 조회까지 동작
btnRegularPro = driver.find_element_by_css_selector(
    "#content > div.content > form:nth-child(2) > div.original_apt > div.tbl_normal > table > tbody > tr:nth-child(1) > td.center > button"
).click()
time.sleep(1)
selectTestName = driver.find_element_by_css_selector(
    "#content > div.content > form > div > table > tbody > tr:nth-child(2) > td > select > option:nth-child(93)"
).click()
time.sleep(1)
nextBtn = driver.find_element_by_css_selector("#btnGoNext").click()
time.sleep(1)
selectRegion = driver.find_element_by_css_selector(
    "#sido > option:nth-child(3)"
).click()
time.sleep(1)
selectApplicantType = driver.find_element_by_css_selector(
    "#recptCd > option:nth-child(2)"
).click()
time.sleep(1)

flag = True

while flag:
    searchBtn = driver.find_element_by_css_selector(
        "#content > div.content > div > form > div > table > tbody > tr:nth-child(4) > td > button"
    ).click()
    time.sleep(1)

    # 조회 후 데이터 찾기
    dataTable = driver.find_element_by_xpath(
        "//*[@id='DIV2']/div[1]/table/tbody")

    for tr in dataTable.find_elements_by_tag_name("tr"):
        td = tr.find_elements_by_tag_name("td")
        s = "td5: {} , \n td7: {}".format(
            td[5].text, re.findall("\d+", td[7].text))
        print(s)
        print("---------------------------------------------------")
        if config.place in td[5].text and int(re.findall("\d+", td[7].text)[0]) > 0:
            telegramBot.telegramHandler(
                td[5].text, re.findall("\d+", td[7].text)[0]
            )
            print("Success!!!!!")
            flag = False
            break
