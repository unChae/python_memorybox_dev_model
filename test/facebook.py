import urllib.request, urllib.parse, urllib.error
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import time
import json
from collections import OrderedDict

# 페이스북 데이터 다운로드 요청 코드
# 페이스북 로그인 URL
Facebook_loginUrl = 'https://www.facebook.com/login/'

# driver load
driver = wd.Firefox(executable_path='D:\geckodriver')

driver.implicitly_wait(5)

# 웹 사이트 접속
driver.get(Facebook_loginUrl)


# 로그인 
driver.find_element_by_name('email').send_keys(Facebook_name)
driver.find_element_by_name('pass').send_keys(Facebook_pw)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="loginbutton"]').submit()

# 설정 클릭 후 데이터 다운로드 요청
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/i').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/div/span').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/a/div[1]/div[2]/div/div/div/div/span').click()
driver.get('https://www.facebook.com/dyi/?referrer=yfi_settings')

# 다운 파일 형식 JSON으로 바꾸기





#driver.find_element_by_name('이메일').send_keys(insta_user_email)
#driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div/button').click()
#driver.find_element_by_name('password').send_keys(insta_user_pw)
#driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div/button').click()

#인스타는 다운 이메일 보내고 다시 로그인 후 다운 링크 클릭