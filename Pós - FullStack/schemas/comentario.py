from pydantic import BaseModel, validator
from typing import Optional, List
from model import Session, Passeio, Cliente
from model.comentario import Comentario

class ComentarioSchema(BaseModel):
    """ Define como um novo Comentario a ser inserido deve ser representado
    """
    passeio_id: int = 1
    cliente_nome: str = "Lucimere Maria"
    texto: str = "Passeio foi lindo, o Guia é super simpático"

    @validator("passeio_id")
    def valida_passeio_id(cls, v):
        session = Session()
        passeio = session.query(Passeio).filter(Passeio.id == v).first()
        print(passeio)
        if not passeio:
            raise ValueError('Passeio não encontrado na base :/')
        return v
        
    @validator("cliente_nome")
    def valida_cliente(cls, v):
        session = Session()
        cliente = session.query(Cliente).filter(Cliente.nome == v).first()
        if not cliente:
            raise ValueError('Cliente não encontrado na base :/')
        return v

class ComentarioViewSchema(BaseModel):
    """ Define como um registro de Comentario deverá ser retornado
    """
    id: int = 10 
    cliente_nome: str = "Vera Lucia"
    texto: str = "Passeio foi lindo, o Guia é super simpático"

class ComentarioDelSchema(BaseModel):
    """ Define como um novo Comentario a ser inserido deve ser representado
    """
    id: int = 10

def apresenta_comentario(comentario: Comentario):
    """ Retorna uma apresentação do produto seguindo o schema
        definido em ComentarioViewSchema   
    """
    return {
        "id": comentario.id,
        "passeio_id": comentario.passeio_id,
        "cliente_nome": comentario.cliente_nome,
        "texto": comentario.texto
    }