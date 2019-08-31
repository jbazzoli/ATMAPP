#!/usr/bin/env python
from urllib2 import urlopen
import sys

# Definicao da chamada das rotas do Banco
# Tratamento das entradas por linha de comando dos parameytros de cada operacao,  requisiscao e apresentacao do resultado
def banco(machine, port, op):	
	url = "http://"+machine+":"+port
	if op == 'deposit':
		conta = sys.argv[5]
		valor = sys.argv[6]
		cliente = sys.argv[4]
		url += "/deposit/"+cliente+"/"+conta+"/"+valor
	elif op == 'withdraw':
		conta = sys.argv[5]
		valor = sys.argv[6]
		cliente = sys.argv[4]
		url += "/withdraw"+"/"+cliente+"/"+conta +"/"+valor
	elif op == 'begin_transaction':
		conta = sys.argv[4]
		url += "/begin_transaction/"+conta
	elif op == 'inquiry':
		conta = sys.argv[4]
		url += "/inquiry/"+conta
	elif op == 'end_transaction':
		conta = sys.argv[4]
		url +="/end_transaction/"+conta
	else:
		print("Invalid option")

	print(url)
	response = urlopen(url)
	data = response.read().decode("utf-8")
	print(data)

def main():
	# parametros do servidor
	machine = sys.argv[1]
	port = sys.argv[2]
	por = 5000
	# operacao a ser realizada
	op = sys.argv[3]
	banco(machine, port, op)

main()
