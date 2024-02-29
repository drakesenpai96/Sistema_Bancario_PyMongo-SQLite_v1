from classesBancoSQLite import Base, Cliente, Conta
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session
import random

print('Conectando ao SQLite...')
conn = create_engine('sqlite:///memory', echo=True)
print('Conectado !!')

ss = Base.metadata.create_all(conn)

session = Session(conn)

def listar_contas():
    cpf = int(input(f"""
        {str(" LISTAR CONTAS ").center(40, "-")}
    

Digite seu cpf => """).replace('.', '').replace('-', ''))
    
    check = session.scalar(select(Cliente).where(Cliente.cpf.in_([cpf])))
    
    if not str(type(check)) == "<class 'NoneType'>":
        contas = session.scalar(select(Conta).where(Conta.id_cliente.in_([check.id])))
        try:
            for conta in contas:
                print(conta)
            return
        except:
            return


#CRIAR CONTA 
def menu_criar_conta():
    cpf = int(input(f"""
        {str(" CRIAR CONTA ").center(40, "-")}
    

Digite seu cpf => """).replace('.', '').replace('-', ''))
    
    check = session.scalar(select(Cliente).where(Cliente.cpf.in_([cpf])))
    
    if not str(type(check)) == "<class 'NoneType'>":
        try:
            nConta = Conta(
                tipo='CONTA-CORRENTE',
                agencia=1000,
                num_conta = random.randint(1, 10000000),
                id_cliente = check.id,
                saldo=0.0
            )

            session.add(nConta)
            session.commit()
            print('Conta criada com sucesso !!')

        except:
            nConta = Conta(
                tipo='CONTA-CORRENTE',
                agencia=1000,
                num_conta = random.randint(1, 10000000),
                id_cliente = check.id,
                saldo=0.0
            )

            session.add(nConta)
            session.commit()
            print('Conta criada com sucesso !!')
    else:
        print('CPF invalido ou nao cadastrado!\nTente novamente')



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
    
        nCli = Cliente(
            nome=nome,
            cpf=cpf,
            endereco=endereco
        )
        session.add(nCli)
        session.commit()
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
