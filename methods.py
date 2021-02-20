import requests

def get(url, params=None):
	try:
		response_get = requests.get(url, params=params)
		print('\nRequest enviado com sucesso!')
		print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
		print(f'\nResponse: \n\n{response_get.text}\n')
		print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
	except:
		print('Ocorreu um erro ao tentar executar a ação!')

def post(url, conteudo=None, params=None, quantidade=1):
	try:
		for post_request in range(quantidade):
			response_post = requests.post(url, data=conteudo, params=params)
			print('\nRequest enviado com sucesso!')
		print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
		print(f'\nResponse: \n\n{response_post.text}\n')
		print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
	except:
		print('\nOcorreu um erro ao tentar executar a ação!\n')

def put(url, conteudo=None):
	try:
		response_put = requests.put(url, data=conteudo)
		print('\nRequest enviado com sucesso!')
		print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
		print(f'\nResponse: \n\n{response_put.text}\n')
		print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
	except:
		print('Ocorreu um erro ao tentar executar a ação!')

def delete(url):
	try:
		response_delete = requests.delete(url)
		print('\nRequest enviado com sucesso!')
		print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
		print(f'\nResponse: \n\n{response_delete.text}\n')
		print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
	except:
		print('Ocorreu um erro ao tentar executar a ação!')