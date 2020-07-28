import requests
from bs4 import BeautifulSoup


def get_mean(word):
    url = 'https://dic.daum.net/search.do'
    params = {
        'q': word,
    }
    res = requests.get(url, params=params)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.select_one('.list_search').text.strip()
