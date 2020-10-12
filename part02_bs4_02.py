# -*- coding: utf-8 -*-

## 01 URL을 확보
## 02 URL에서 HTML정보를 얻어온다
## 03 얻어온 정보를 bs4를 이용하여 구조화한다.
## 04 soup.find, soup.find_all 함수등

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://finance.naver.com/sise/"

page = urlopen(url)
#PRINT(page)
soup = BeautifulSoup(page, 'html.parser')

#%%정보가져오기
# 네이버 코스피 코스닥, 코스피200
kospi = soup.find("span", id = "KOSPI_now").text
print("현재 코스피 지수는 {} 입니다.".format(kospi))

#%% 실습 3-2 코스닥, 코스피200지수 가져오기
# KOSDAQ_now
# KPI200_now
KOSDAQ = soup.find("span", id="KOSDAQ_now").text
KPI200 = soup.find("span", id="KPI200_now").text
print("현재 코스닥 지수는 {} 입니다. ".format(KOSDAQ))
print("현재 코스피200 지수는 {} 입니다. ".format(KPI200))

#%% 실습 3-3 인기검색종목 10개
#tag명 ul
# class lst_pop
li_all = soup.find("ul", class_="lst_pop")
# print(li_all)

a_all = li_all.find_all("a")

for i in a_all:
    print(i.text)
    
#%%

