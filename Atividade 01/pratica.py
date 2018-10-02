from bs4 import BeautifulSoup
import requests
import re
import parser

def search(keyword, url, deth, links_visitados):

    #Download da página e armazenamento dos links
    try:
        print('\naguarde...')
        response = requests.get(url)
        links_visitados.append(url)
        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
    except:
        print("Link inválido: ", url)
        links = []

    #busca de ocorrencias da keyword na pagina
    if html.text.upper().__contains__(keyword.upper()):
        pattern = re.compile('.{0,100}%s.{0,100}' % keyword.upper())
        result_ini = [m.start() for m in re.finditer(pattern, html.text.upper())]
        result_fim = [m.end() for m in re.finditer(pattern, html.text.upper())]

        qtd_resultados = html.text.upper().count(keyword.upper())
        print("\n%d resultado(s) em %s: " %(qtd_resultados, url))

        for i in range(len(result_ini)):
            print('%d. %s' % (i+1, html.text[result_ini[i] : result_fim[i]]))

    #verificacao para recursividade
    if deth > 0:
        for link in links:
            try:
                if link['href'].startswith('http') and link['href'] not in links_visitados:
                    search(keyword, link['href'], deth - 1, links_visitados)
            except:
                pass


def main():
    keyword = input('Digite uma keyword: ')
    link = input('Digite uma URL base: http://')
    deth = int(input('Informe a profundidade: '))
    links_visitados = []

    url = "http://" + link
    palavra_chave = " %s " %keyword

    search(palavra_chave, url, deth, links_visitados)


if __name__ == '__main__':
    main()