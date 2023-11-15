# SELENIUM

# pip install selenium
# pip install webdriver_manager

# ** Selenum을 사용하는 이유?
#   - Requests는 현재 URL의 정적 페이지 소스코드만 수집 가능
#       → "더보기" 버튼 클릭과 같이 동적인 동작 불가!
#   - Selenium은 전용 브라우저를 사용해서 동작
#       → 따라서 chrome 드라이버와 같이 브라우저 설정 반드시 필요!
#   ※ Selenium은 처음에 웹 브라우저 테스트 용으로 개발

# ** Selenium 사용 방법 2가지
#   1.직접 다운로드
#   - URL: https://sites.google.com/chromium.org/driver/
#   2.실시간(코드) 다운로드


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. Selenium 전용 웹 브라우저 구동
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
# 2. URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=165591"
driver.get(url)

# 3. 페이지 전체 코드 가져오기
doc_html = driver.page_source
print(doc_html)

# 4. Selenium → BeutifulSoup
doc = BeautifulSoup(doc_html, "html.parser")

# 5. 영화 제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()
print(movie_title)