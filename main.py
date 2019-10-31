from search_scraper import search_duckduckgo


if __name__ == '__main__':
    word = input('¿Que quieres buscar en duckduckgo?:')
    results = search_duckduckgo(word)
    for r in results:
        print('-----------******************************------------')
        print('Title:{}Url:\n{}\nDescription:\n{}'.format(r['title'], r['url'], r['description']))


