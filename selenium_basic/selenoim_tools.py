# 1. 가상환경 실행하기
    # 1) python -m virtualvenv venv
    # 2) 가상환경 실행 venv/Scripts/activate
# 2. 셀레니움 설치


# 3. 크롬 실행하기
    # 1) drver.get(url)
    # 2) 개발자도구 열기 : ctrl shift i
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller


 # 시스템에 부착된 장치가 작동하지 않습니다 해결 1

chromedriver_autoinstaller.install()

 # 시스템에 부착된 장치가 작동하지 않습니다 해결 1
driver = webdriver.Chrome()
# 1. Navigtaion


# 1.1 get
driver.get("https://www.naver.com")
time.sleep(3)
driver.get("https://google.com")

# 1.2 back
driver.back()
time.sleep(3)
# 1.3 forward()
driver.forward()
time.sleep(3)
# 1.4 refresh()
driver.refresh()
time.sleep(3)

# 2. browser information
# 2-1. title : 웹사이트 타이틀 가져오기
타이틀 = driver.title
print(타이틀, "현재 타이틀")
# 2-2. current_url
주소 = driver.current_url
print(주소, "현재주소")

# 3. Driver Wait
# 10초 까지는 element를 찾는 것을 기다림, 10초 넘어가면 에러 던짐
try :
    selector = "#NM_THEME_CONTAINER > div.theme_tab > ul"
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
        By.CSS_SELECTOR, selector
))
except : 
    print("다음 코드 실행")
navigation = driver.find_element(By.CSS_SELECTOR, selector)
print(navigation.text)
input()
#NM_THEME_CONTAINER > div.theme_tab > ul