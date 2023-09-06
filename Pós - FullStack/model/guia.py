from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from typing import Union

from  model import Base, Passeio


class Guia(Base):
    __tablename__ = 'guia'

    id: Mapped[int] = Column("pk_guia", Integer, primary_key=True)
    nome: Mapped[str] = Column(String(140), unique=True)
    telefone: Mapped[str] = Column(String(40))
    email: Mapped[str] = Column(String(60))
    transporte: Mapped[str] = Column(String(40))
    data_insercao: Mapped[str] = Column(DateTime, default=datetime.now())

    passeios = relationship("Passeio", backref="guia")


    def __init__(self, nome:str, telefone:str, email:str, transporte:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um guia

        Arguments:
            nome: nome do guia.
            telefone: telefone do guia
            email: email do guia
            transporte: transporte do guia
            data_insercao: data de quando o guia foi inserido à base
        """
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.transporte = transporte

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
