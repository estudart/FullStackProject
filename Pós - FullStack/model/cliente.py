from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from typing import Union

from model import Base, Passeio


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    telefone = Column(String(40))
    email = Column(String(60))
    data_insercao = Column(DateTime, default=datetime.now())

    passeios = relationship("Passeio", backref="cliente")

    def __init__(self, nome:str, telefone:str, email:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um cliente

        Arguments:
            nome: nome do cliente.
            telefone: telefone do cliente
            email: email do cliente
            data_insercao: data de quando o cliente foi inserido à base
        """
        self.nome = nome
        self.telefone = telefone
        self.email = email

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

