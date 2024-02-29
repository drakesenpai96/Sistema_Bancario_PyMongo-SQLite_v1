from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, inspect, select, func
from sqlalchemy.orm import Session, declarative_base, relationship, create_session

Base =  declarative_base()


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(Integer, unique=True, nullable=False)
    endereco = Column(String, nullable=False)

    def __repr__(self):
        return f"""
    Nome : {self.nome}
    CPF: {self.cpf}
    Endereco: {self.endereco}
"""
    
class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False)
    agencia = Column(Integer, nullable=False)
    num_conta = Column(Integer, unique=True, nullable=False)
    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    saldo = Column(Float, nullable=False)

    def __repr__(self):
        return f"""
    Tipo da conta: {self.tipo}
    Agencia: {self.agencia}
    Numero da conta: {self.num_conta}
    Saldo: {self.saldo} 
"""

