import urllib.request, urllib.parse, urllib.error
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import time
import json
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

# 인스타그램 데이터 다운로드 요청 코드
# 인스타그램 로그인 URL
insta_loginUrl = 'https://www.instagram.com/accounts/login/'

# driver load
CHROMEDRIVER_PATH = './chromedriver.exe'

chrome_options = Options()

# hide windows
# chrome_options.add_argument('headless')
# chrome_options.add_argument('window-size=1920x1080')
# chrome_options.add_argument("disable-gpu")

driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )

driver.implicitly_wait(5)

# 웹 사이트 접속
driver.get(insta_loginUrl)



# 로그인 정보 입력
driver.find_element_by_name('username').send_keys(insta_user_name)
driver.find_element_by_name('password').send_keys(insta_user_pw)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').submit()


# 정보저장 안함 클릭
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div').click()
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

# 데이터 이메일로 다운로드 요청 코드
driver.get('https://www.instagram.com/download/request/')
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div/button').click()
time.sleep(1)
driver.find_element_by_name('password').send_keys(insta_user_pw)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div/button').click()

#인스타는 다운 이메일 보내고 다시 로그인 후 다운 링크 클릭

