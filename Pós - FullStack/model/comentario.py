from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Comentario(Base):
    __tablename__ = 'comentario'

    id = Column("pk_comentario", Integer, primary_key=True)
    texto = Column(String(4000))
    cliente_nome = Column(String(50))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o comentário e um passeio.
    # Aqui está sendo definido a coluna 'passeio' que vai guardar
    # a referencia ao passeio, a chave estrangeira que relaciona
    # um passeio ao comentário.

    passeio_id = Column(Integer, ForeignKey("passeio.pk_passeio"), nullable=False)

    def __init__(self, texto:str, cliente_nome: str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Comentário

        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.cliente_nome = cliente_nome
        self.texto = texto
        if data_insercao:
            self.data_insercao = data_insercao
