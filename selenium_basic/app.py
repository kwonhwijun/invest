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
import chromedriver_autoinstaller


 # 시스템에 부착된 장치가 작동하지 않습니다 해결 1

chromedriver_autoinstaller.install()

 # 시스템에 부착된 장치가 작동하지 않습니다 해결 1
driver = webdriver.Chrome()
#1. 네비게이션 : 웹사이트의 주소를 바꾸는 역할(새로고침 포함)
driver.get("https://www.naver.com")
time.sleep(3)

# 개발자도구(ctrl shift i)에서 요소(selector) 가져오기
css_selector = "#NM_FAVORITE > div.group_nav"

# 2-2. 찾아온 요소를 가져오기
group_nav = driver.find_element(By.CSS_SELECTOR, css_selector)

# 3-1. 데이터를 가져오기
print(group_nav.text)

# 3-2. 요소 클릭하기
group_nav.click()
input()

#NM_THEME_CONTAINER > div.theme_tab > ul