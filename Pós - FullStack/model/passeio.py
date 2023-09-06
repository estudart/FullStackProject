from sqlalchemy import Column, String, Integer, DateTime, ForeignKeyConstraint, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Passeio(Base):
    __tablename__ = 'passeio'

    id = Column("pk_passeio", Integer, primary_key=True)
    guia_nome = Column(String(100), ForeignKey("guia.nome"), nullable=False)
    lugar_nome = Column(String(100), ForeignKey("lugar.nome"), nullable=False)
    cliente_nome = Column(String(100), ForeignKey("cliente.nome"), nullable=False)
    n_estrela = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())


    # Definição do relacionamento entre o passeio e o comentário.
    # Essa relação é implicita, não está salva na tabela 'passeio',
    # mas aqui estou deixando para SQLAlchemy a responsabilnomeade
    # de reconstruir esse relacionamento.

    comentarios = relationship("Comentario")

    def __init__(self, guia_nome:int, lugar_nome:str, cliente_nome:str, n_estrela:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um passeio

        Arguments:
            guia: guia do passeio.
            quantnomeade: quantnomeade que se espera comprar daquele passeio
            valor: valor esperado para o passeio
            data_insercao: data de quando o passeio foi insernomeo à base
        """
        self.guia_nome = guia_nome
        self.lugar_nome = lugar_nome
        self.cliente_nome = cliente_nome
        self.n_estrela = n_estrela

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
    
    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao lugar
        """
        self.comentarios.append(comentario)

