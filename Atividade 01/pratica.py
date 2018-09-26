from bs4 import BeautifulSoup
import requests
import re
import parser


def search(keyword, url, deth):
    # baixar a pagina html

    try:
        print('aguardando ', url, '...')
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
    except:
        print("Link inválido: ", url)
        links = []

    if html.text.__contains__(keyword):
        pattern = re.compile('.{0,50}%s.{0,50}' % keyword)
        result = re.search(pattern, html.text)
        print(result.group())

    if deth > 0:
        for link in links:
            try:
                if link['href'].startswith('http'):
                    search(keyword, link['href'], deth - 1)
            except:
                pass


def main():
    # keyword = input('Digite uma keyword: ')
    # url = input('Digite uma URL base: ')
    # deth = int(input('Informe a profundidade: '))

    search('reitor', 'http://libra.ifpi.edu.br', 3)


if __name__ == '__main__':
    main()