import requests
from methods import get, post, put, delete

while True:
	print('Escolha uma método abaixo')
	print('\n[1] Get')
	print('[2] Post')
	print('[3] Put')
	print('[4] Delete')
	print('[3] Sair\n')
	opcao = int(input('Opcao: '))
	if opcao == 1:
		url = input('\nURL: ')
		params = input('Parâmetros: ')
		get(url, params)
	elif opcao == 2:
		url = input('\nURL: ')
		conteudo = input('Data: ')
		params = input('Parâmetros: ')
		quantidade = int(input('Quantidade de requests: '))
		post(url, conteudo, params, quantidade)
	elif opcao == 3:
		url = input('\nURL: ')
		conteudo = input('Data: ')
		put(url, conteudo)
	elif opcao == 4:
		url = input('\nURL: ')
		delete(url)
	elif opcao == 5:
		quit()
	else:
		print('\nOpção Inválida!')