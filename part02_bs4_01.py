# -*- coding: utf-8 -*-

#%%
from bs4 import BeautifulSoup

page = open("mypage1012.html", 'r', encoding="utf-8").read()
print(page)

soup = BeautifulSoup(page, "html.parser")
print(soup)

#%%
#헤드라인1을 하나 가져오기
data = soup.find("h1")
print(data.text)

#단락1 정보 가져오기
p1 = soup.find("p")
print(p1.text)

#%% 
link_txt =soup.find("a")
print(link_txt.text)

#%% a 태그로 연결된 전체정보 가져온다.
# all전체정보 리스트를 갖고 오게 된다.
link_all = soup.find_all('a')
print(link_all)

for i in link_all:
    print(i.text)
#%% 실습 3-1 p태그 전체 정보를 가져와서, text출력해 보기
link_p = soup.find_all('p')
for i in link_p:
    print(i.text)

#%%네이버 가져오기
link_p  = soup.find_all("a")   
print(link_p[2].text)