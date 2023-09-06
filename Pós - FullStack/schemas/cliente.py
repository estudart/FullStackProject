from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente

class ClienteSchema(BaseModel):
    """ Define como um novo Cliente a ser inserido deve ser representado
    """
    nome: str = "Lucimere Maria"
    telefone: str = "2197-5550"
    email: str = "lucimere.maria@gmail.com"

class ClienteViewSchema(BaseModel):
    """ Define como um registro de cliente deverá ser retornado
    """
    id: int = 4
    nome: str = "Lucimere Maria"
    telefone: str = "2197-5550"
    email: str = "lucimere.maria@gmail.com"

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma apresentação do produto seguindo o schema
        definido em ClienteViewSchema   
    """
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "telefone": cliente.telefone,
        "email": cliente.email
    }
