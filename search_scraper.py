import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.INFO)


HEADER = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/77.0.3865.120 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }


def search_duckduckgo(word):
    """
    Return fisrt ten search.
    """
    logging.info(f'Searching  {word} in Duckduckgo...')

    url = 'https://duckduckgo.com/html/'
    query = {'q': word}
    session = requests.Session()
    response = session.get(url, params=query, headers=HEADER)

    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all('div', {'class': 'result results_links results_links_deep web-result'})

    search_list = []
    count = 0

    for result in results:
        count += 1
        title = result.find('h2', 'result__title').text
        url = result.find('a', 'result__a')['href']
        description = result.find('a', 'result__snippet').text
        if count <= 10:
            search_list.append({'title': title, 'url': url, 'description': description})
    return search_list
