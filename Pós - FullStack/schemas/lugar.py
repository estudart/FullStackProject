from pydantic import BaseModel
from typing import Optional, List
from model.lugar import Lugar

class LugarSchema(BaseModel):
    """ Define como um novo Lugar a ser inserido deve ser representado
    """
    nome: str = "Praia de Itacoatiara"
    tipo: str = "Praia"

class LugarViewSchema(BaseModel):
    """ Define como um registro de Lugar deverá ser retornado
    """
    id: int = 4
    nome: str = "Praia de Itacoatiara"
    tipo: str = "Praia"

def apresenta_lugar(lugar: Lugar):
    """ Retorna uma apresentação do produto seguindo o schema
        definido em ClienteViewSchema   
    """
    return {
        "id": lugar.id,
        "nome": lugar.nome,
        "tipo": lugar.tipo
    }
