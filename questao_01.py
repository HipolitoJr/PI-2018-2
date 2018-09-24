import requests

url = input("Informe uma URL: ")

try:
    response = requests.get(url)

    print('Status code: ', response.status_code)
    print('Cabeçalhos: ', response.headers)
    print('Tamanho da resposta: ', response.headers['Content-Length'])

except:
    print("URL inválida")