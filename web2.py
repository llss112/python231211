#web2.py

import requests
# 크롤링
from bs4 import BeautifulSoup

url="https://www.daangn.com/fleamarket/?_fp=20b4cd02bcac71586b5603a2b8b85f17"

response=requests.get(url)

# 검색이 용이한 객체
soup=BeautifulSoup(response.text,"html.parser")
posts=soup.find_all("div",attrs={"class":"card-desc"})

#파일에 저장
f=open("dangn.txt","wt",encoding="utf-8")
for post in posts:
    title=post.find("h2",attrs={"class":"card-title"})
    price=post.find("div",attrs={"class":"card-price"})
    addr=post.find("div",attrs={"class":"card-region-name"})
    title=title.text.strip().replace("\n","")
    price=price.text.strip().replace("\n","")
    addr=addr.text.strip().replace("\n","")
    print("{0},{1},{2}".format(title,price,addr))
    f.write(f"{title},{price},{addr}\n")

# <div class="card-desc">
#       <h2 class="card-title">몽클레어 여성패딩</h2>
#       <div class="card-price ">
#         190,000원
#       </div>
#       <div class="card-region-name">
#         경기도 성남시 분당구 정자동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 57
#           </span>
#         ∙
#         <span>
#             채팅 32
#           </span>
#       </div>
#     </div>


