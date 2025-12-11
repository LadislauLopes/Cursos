import requests

def informacoes_cnpj(cnpj):
  url_base = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
  json=requests.get(url_base).json()
  return json