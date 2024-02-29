import pymongo
import bson
from datetime import datetime
import random

client = pymongo.MongoClient('localhost:27017')

banco = client.app_banco
clientes = banco.clientes


def listar_contas():
    cpf = int(input(f"""
        {str(" LISTAR CONTAS ").center(40, "-")}
    

Digite seu cpf => """).replace('.', '').replace('-', ''))
    
    check = clientes.find_one({'cpf': cpf})
    
    if not str(type(check)) == "<class 'NoneType'>":
        try:
            for conta in check['contas']:
                print(conta)
            return
        except:
            return


#CRIAR CONTA 
def menu_criar_conta():
    cpf = int(input(f"""
        {str(" CRIAR CONTA ").center(40, "-")}
    

Digite seu cpf => """).replace('.', '').replace('-', ''))
    
    check = clientes.find_one({'cpf' : cpf})
    
    if not str(type(check)) == "<class 'NoneType'>":
        id = check['_id']
        conta = {
            'tipo' : 'CONTA-CORRENTE',
            'agencia' : 1000,
            'num_conta' : random.randint(1, 10000000),
            'saldo' : 0.0
        }

        check['contas'].append(conta)

        clientes.update_one({'_id': id}, {'$set': check})



#CRIAR USUARIO
def menu_criar_usuario():
    nome = input(f"""
        {str(" CRIAR USUARIO ").center(40, "-")}
    

Digite seu nome completo => """)
    

    cpf = int(input("Digite seu CPF => ").replace('.', '').replace('-', ''))

    logradouro = input("Digite o logradouro da sua residencia => ") 

    num = input("Digite o numero da sua residencia => ")

    bairro = input("Digite seu bairro => ")

    cidade = input('Digite sua cidade => ')

    siglaEstado = input("Digite a sigla do seu estado (ex : RJ) =>")


    endereco = f'{logradouro},{num} - {bairro} - {cidade}/{siglaEstado}'

    try:
    
        nCli = {
            'nome' : nome,
            'cpf' : cpf,
            'endereco' : endereco,
            'contas' : []
        }
        clientes.insert_one(nCli)

        print('Usuario criado com sucesso !!\nVoltando para o menu')
    except:
        print('Usuario ja existe')
        return
    


#MENU INICIAL
def menu_inicial():
    try:
        opcao = input(f"""
            {str(" BANCO INTERNACIONAL ")}
        
        Opcoes:

        [1] Criar usuario
        [2] Criar conta
        [3] Listar contas
        [0] Sair

    Digite uma opcao => """)
        
        if int(opcao) == 1:
            menu_criar_usuario()
            return True
        
        elif int(opcao) == 2:
            menu_criar_conta()
            return True     

        elif int(opcao) == 3:
            listar_contas()
            return True

        elif int(opcao) == 0:
            return False

    except Exception as error:
        print(f"{error}\n\n")


menu_inicial()

while True:    
    if menu_inicial():
        continue
    else:
        break