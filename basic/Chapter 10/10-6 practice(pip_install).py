# pypi 에서 패키지 참조
# 맥에서 패키치 설치 할때는 pip3를 참고해라! 꼭! 맥에는 파이썬2가 설치되어 있어 꼭 3를 써주는게 좋음
# beautifulsoup4 참고

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())