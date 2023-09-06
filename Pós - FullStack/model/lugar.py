from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from typing import Union

from  model import Base, Comentario, Passeio


class Lugar(Base):
    __tablename__ = 'lugar'

    id = Column("pk_lugar", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    tipo = Column(String(40))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o lugar e o comentário.
    # Essa relação é implicita, não está salva na tabela 'lugar',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    # comentarios = relationship("Comentario")

    passeios = relationship("Passeio", backref="lugar")

    def __init__(self, nome:str, tipo:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um lugar

        Arguments:
            nome: nome do lugar.
            tipo: tipo de lugar que é o roteiro
            data_insercao: data de quando o lugar foi inserido à base
        """
        self.nome = nome
        self.tipo = tipo

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    # def adiciona_comentario(self, comentario:Comentario):
        # """ Adiciona um novo comentário ao lugar
        # """
        # self.comentarios.append(comentario)

