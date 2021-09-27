import requests

def retorna_dados_cep (cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

def retorna_response (url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://globallab.org/en/#.YU-bgbhKhPY')
    print(response)
    #retorna_dados_cep('01001000')
