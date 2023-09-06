from pydantic import BaseModel
from typing import Optional, List
from model.guia import Guia

class GuiaSchema(BaseModel):
    """ Define como um novo Guia a ser inserido deve ser representado
    """
    nome: str = "Marco Aurelio"
    telefone: str = "21 99937-0735"
    email: str = "marco.aurelio@gmail.com"
    transporte: str = "Troller"

class GuiaViewSchema(BaseModel):
    """ Define como um registro de Guia deverá ser retornado
    """
    id: int = 1
    nome: str = "Marco Aurelio"
    telefone: str = "21 99937-0735"
    email: str = "marco.aurelio@gmail.com"
    transporte: str = "Troller"

def apresenta_guia(guia: Guia):
    """ Retorna uma apresentação do produto seguindo o schema
        definido em GuiaViewSchema   
    """
    return {
        "id": guia.id,
        "nome": guia.nome,
        "telefone": guia.telefone,
        "email": guia.email,
        "transporte": guia.transporte
    }