import requests  # Import requests
from bs4 import BeautifulSoup  # Import BeautifulSoup4

# Windows 10 with Google Chrome
user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

headers = {'User-Agent': user_agent_desktop}

url_twitter = 'https://www.amazon.in/dp/B08WC387F8/ref=pc_mcnc_merchandised-search-12_?pf_rd_s=merchandised-search-12&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=5ADV9ZM5QGV3JX45DDJ9&pf_rd_p=e7024920-7ae9-40db-97a4-252e126f2590'
resp = requests.get(url_twitter, headers=headers)  # Send request

code = resp.status_code  # HTTP response code
if code == 200:
    soup = BeautifulSoup(resp.text, 'lxml')  # Parsing the HTML
    print(soup.prettify())
else:
    print(f'Error to load Twitter: {code}')
