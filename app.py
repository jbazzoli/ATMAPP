#!flask/bin/python
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/begin_transaction/<cutm>', methods=['GET'])
def begin_transaction(cutm):
	if cutm in cliente:
		return "Customer " + cutm + " starts his transaction."
	else: 
		return "Customer not found!"
def block(cutm, acnt):
	for i in banco:
		if i==acnt:
			if (not bloqueio[acnt]):
				bloqueio[acnt]=1
				cl_to_ba[cutm]=acnt		
				return "Conta bloqueada para operacoes!"
	return "Transaction is already running for account " + cutm
	
@app.route('/end_transaction/<cutm>', methods=['GET'])
def end_transaction(cutm):
        if tmp[cl_to_ba[cutm]] != None:
                banco[cl_to_ba[cutm]] = tmp[cl_to_ba[cutm]]
                tmp[cl_to_ba[cutm]] = None
	return unBlock(cl_to_ba[cutm],cutm)
	
@app.route('/abort_transaction/<cutm>', methods=['GET'])
def abort_transaction(cutm):
	return unBlock(cl_to_ba[cutm],cutm)
	
def unBlock(acnt,cutm):
	for i in banco:
		if i==acnt:
			bloqueio[acnt]=0
			cl_to_ba[cutm]=0
			return "Conta Desbloqueada para outro usuario"
	return "Transacao nao comecada para ser terminada"
#def abort_transaction(cutm):
#nao sei como implementar esse metodo eh estranho

def withdraw_local(conta, valor):
	if conta in banco:
		debit = banco[conta] - int(valor)
		if debit >= 0:
			tmp_value = temp_value + {conta : debit}
			result = True #sucesso
		else:
			result = False #saldo insufciente
	else:
		result = False #conta nao existe
	return result
	
#Realiza as operacoes de deposito na estrutura de dados
def deposito_local(conta, valor):
	if conta in banco:
	        tmp_value = temp_value + {conta : int(valor)}
		result = True #sucesso
	else:
		result = False #conta nao existe
	return result

@app.route('/withdraw/<cutm>/<acnt>/<amt>', methods=['GET'])
def withdraw(cutm,acnt,amt):
	if bloqueio[acnt] and cl_to_ba[cutm]==acnt and (acnt in banco) and withdraw_local(acnt, amt):
	        block(cutm,acnt)
		result = "Succesfully withdraw S" + amt + " from account " + acnt + "!"
	else:
		result = "Ou usuario {0} nao existe ou saldo insuficiente para saque ou conta nao bloqueada para este usuario".format(cliente[cutm])
	return result

@app.route('/deposit/<cutm>/<acnt>/<amt>', methods=['GET'])
def deposit(cutm,acnt,amt):
	if bloqueio[acnt] and (cl_to_ba[cutm]==acnt) and (acnt in banco) and deposito_local(acnt, amt):
                        block(cutm,acnt)
		result = "Succesfully deposit $" + amt + " to account " + acnt + "!"
	else:
		result = "Usuario {0} nao existe ou a conta nao foi bloqueda para este usuario".format(cliente[cutm])
	return result

@app.route('/inquiry/<cutm>/<acnt>',methods=['GET'])
def inquiry(cutm, acnt):
	if bloqueio[acnt] and (cl_to_ba[cutm]==acnt) and (acnt in banco):
	        block(cutm,acnt)
		result = "The current balance of account {0} is $ {1}".format(acnt, banco[cutm])
	else:
		result = "Usuario {0} nao existe ou a conta nao foi bloqueada para este usuario ".format(cutm)
	return result

if __name__ == '__main__':
	banco = {"100":1000, "200":2000}
	cliente = { "1":"Joao Antonio","2":"Jacinto Pinto"}
	bloqueio = {"100":0,"200":0}
        cl_to_ba = {"1":0,"2":0}
        tmp_value = {}
	app.run(debug=True)
