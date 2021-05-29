from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
html_text = requests.get(url)
soup = BeautifulSoup(html_text, 'lxml')
#jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
print(html_text)
