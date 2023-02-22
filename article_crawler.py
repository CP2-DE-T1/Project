import json
import requests
from bs4 import BeautifulSoup
# import pandas as pd


login_url='http://3.34.232.234:8000/api/users/sign-in/'
login_data={'username':'admin','password':'admin'}
get_token=requests.post(login_url,data=login_data)
access_token='Bearer '+get_token.json()['token']['access']
    
    
board_url='http://3.34.232.234:8000/api/boards/'
    
# for page in range(50):
#     article_url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%20%EC%B1%84%EC%9A%A9&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=14&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}1'
#     headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*', 'Authorization':access_token}
#     response=requests.get(article_url)
#     article_html = BeautifulSoup(response.text,'html.parser')
#     news= article_html.select('div.group_news > ul.list_news > li div.news_area > a')
#     for i in news:
#         body={'title':[],
#         'content':[]}
#         contents=requests.get(i.attrs['href'])
#         contents=BeautifulSoup(contents.text,'html.parser')
#         body['title'].append(i.attrs['title'])
#         body['content'].append(contents.find_all('p'))
#         try:
#             response = requests.post(board_url,headers=headers, data=body)
#             print('response status %r' % response.status_code)
#             print('response text %r' % response.text)
#         except Exception as ex:
#             print(ex)
    
    
article_url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%20%EC%B1%84%EC%9A%A9&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=14&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1'
response=requests.get(article_url)
article_html = BeautifulSoup(response.text,'html.parser')
news= article_html.select('div.group_news > ul.list_news > li div.news_area > a')
for i in news:
    contents=requests.get(i.attrs['href'])
    contents=BeautifulSoup(contents.text,'html.parser')
    print(contents.find_all('p'))
    print('=============cut===============')