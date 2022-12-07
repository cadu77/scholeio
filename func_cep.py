import requests, json




def consulta_cep(cep):
    
    url = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    
    
    endereco = url.json()
   

    return endereco['logradouro'], endereco['complemento'], endereco['bairro'], endereco['localidade'], endereco['uf']

#consulta_cep('59066-325')




