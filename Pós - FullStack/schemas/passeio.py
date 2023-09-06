from pydantic import BaseModel, validator
from typing import Optional, List
from model.passeio import Passeio
from model import Session, Lugar, Cliente, Guia

class PasseioSchema(BaseModel):
    """ Define como um novo Passeio a ser inserido deve ser representado
    """
    guia_nome: str = "Marco Aurelio"
    lugar_nome: str = "Praia de Itacoatiara"
    cliente_nome: str = "Lucimere Maria"
    n_estrela: int = 5

    """@validator("guia_nome")
    def valida_guia(cls, v):
        session = Session()
        guia = session.query(Guia).filter(Guia.nome == v).first()
        print(guia)
        if not guia:
            raise ValueError('Guia não encontrado na base :/')
        return v
    
    @validator("cliente_nome")
    def valida_cliente(cls, v):
        session = Session()
        cliente = session.query(Cliente).filter(Cliente.nome == v).first()
        if not cliente:
            raise ValueError('Cliente não encontrado na base :/')
        return v
    
    @validator("lugar_nome")
    def valida_lugar(cls, v):
        session = Session()
        lugar = session.query(Lugar).filter(Lugar.nome == v).first()
        if not lugar:
            raise ValueError('Lugar não encontrado na base :/')
        return v"""      

class PasseioViewSchema(BaseModel):
    """ Define como um registro de Passeio deverá ser retornado
    """
    id: int = 1
    guia_nome: str = "Marco Aurelio"
    lugar_nome: str = "Praia de Itacoatiara"
    cliente_nome: str = "Lucimere Maria"
    n_estrela: int = 5

class PasseioGetSchema(BaseModel):
    """ Define como um registro de Passeio deverá ser retornado
    """
    id: int = 1

class PasseioDelSchema(BaseModel):
    """ Define como um registro de Passeio deverá ser retornado
    """
    id: int = 1

def apresenta_passeio(passeio: Passeio):
    """ Retorna uma apresentação do produto seguindo o schema
        definido em PasseioViewSchema   
    """
    return {
        "id": passeio.id,
        "guia_nome": passeio.guia_nome,
        "lugar_nome": passeio.lugar_nome,
        "cliente_nome": passeio.cliente_nome,
        "n_estrela": passeio.n_estrela
    }