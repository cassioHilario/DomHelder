import requests

url = 'http://44.202.68.190:5000/div/2/4'

r = requests.get(url)

if(r.status_code == 200):
    if r.headers['content-type'] == 'application/json':
        print()
        print('JSON : ', r.json())
        print()
    else:
        print('Conteúdo não estruturado: ',r.text)
else:
    print('Não foi possível conexão com o endereço ', url)