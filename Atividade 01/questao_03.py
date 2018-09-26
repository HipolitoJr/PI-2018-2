import requests
from parse import *

url = input('URL de uma pagina WEB: ')

print('Aguarde a requisição...')
response = requests.get(url)

r = parse("<a href=\"{}\"/>", "<a href=\"https://google.com\"/>")
print(r)

# print('Status code: ', response.status_code)
# print('Arquivo: ', response.headers['content-type'])
