from selenium import webdriver
import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# 1. 네이버 들어가기
driver.get("https://www.naver.com")
time.sleep(1)

# 2. 네이버 로그인 클릭하기
element = driver.find_element(by=By.CLASS_NAME, value = "link_login")
element.click()

# 3.1 아이디 입력
user_id = "huijun96"
user_pw = "96@dufwjd@73"

log_ID = driver.find_element(by=By.ID, value = "id" )
log_ID.click()
pyperclip.copy(user_id)
log_ID.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
# 3.2 PW 입력
log_PW = driver.find_element(by=By.ID, value = "pw")
log_PW.click()
pyperclip.copy(user_pw)
log_PW.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
# 3.3 로그인 클릭
log_ENT = driver.find_element(by = By.ID, value = "log.login")
log_ENT.click()

# 4. 카페로 이동
driver.get("https://cafe.naver.com/gumpark")
input()