import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_opt&sort=0&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") # 결과는 리스트
for link in links:
    title = link.text # 태그 안에 텍스트요소를 가져온다.
    url = link.attrs['href'] # href의 속성값을 가져온다.
    print(title, url)