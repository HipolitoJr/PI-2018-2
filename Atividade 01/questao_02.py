import requests

url_imagem = input('Informe uma URL de imagem: ')

print('Aguarde a requisição...')
response = requests.get(url_imagem)

arq = open('/home/hipolito/Downloads/img%s.jpg' % response.headers['Content-Length'], 'wb')
arq.write(response.content)
arq.close()

print('Status code: ', response.status_code)
print('Arquivo: ', response.headers['content-type'])