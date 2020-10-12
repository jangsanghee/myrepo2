from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"

page = urlopen(url)
soup = BeautifulSoup(page, "lxml")

#%% 
# -->여기부분 복사 안하셔서 안된겁니다.
ul_one=soup.find('ul',class_='lst_detail_t1')
print(ul_one.text)
    
#%%
#li_span = li_all.find_all("span")[1]
#print(li_span)

a_all = ul_one.find_all("a")
print(a_all)

#%% 
# dt, class:tit
#   a -> text
li_all = ul_one.find_all("dt", class_="tit")
# print(li_all[4])

one_title = li_all[50].find("a")
print(one_title.text)

#%%
li_all = ul_one.find_all("dt", class_="tit")

for one in li_all:
    one_title = one.find("a").text
    print(one_title)

##평점 정보가져오기
#01 전체 가져요기
# 02 하나씩 가져오는 것 확인 (어떤태그, 어떤클래스인지)
# 03 for 문으로 돌려보기
ul_one = soup.find("ul", class_="lst_detail_t1")
# print( ul_one )

score_all = ul_one.find_all("span", class_="num")
print(score_all)

#%% 홀수만 가져오기(평점 가져오기)
cnt = 1
for one in score_all:
    if cnt%2==0:
        print(one.text)
    cnt = cnt + 1
    
#%% 예매율 가져오기
cnt = 0
for one in score_all:


