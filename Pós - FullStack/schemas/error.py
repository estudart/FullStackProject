from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """ Define a mensagem de erro que deve ser apresentada
    """
    message: str="Não foi possível salvar novo registro :/"

class ErrorSchemaPasseio(BaseModel):
    """ Define a mensagem de erro que deve ser apresentada
    """
    message: str="Não foi encontrado o passeio na base :/"

class ErrorSchemaGuia(BaseModel):
    """ Define a mensagem de erro que deve ser apresentada
    """
    message: str="Não foi encontrado um Guia com esse nome na base"

class ErrorSchemaGuiaExiste(BaseModel):
    """ Define a mensagem de erro que deve ser apresentada quando um lugar ja existe na base
    """
    message: str="guia de mesmo nome já salvo na base :/"

class ErrorSchemaLugar(BaseModel):
    """ Define a mensagem de erro que deve ser apresentada
    """
    message: str="Não foi encontrado um Lugar com esse nome na base"

class ErrorSchemaLugarExiste(BaseModel):
    """ Define a mensagem de erro que deve ser apresentada quando um lugar ja existe na base
    """
    message: str="lugar de mesmo nome já salvo na base :/"

class ErrorSchemaCliente(BaseModel):
    """ Define a mensagem de erro que deve ser apresentada
    """
    message: str="Não foi encontrado um Cliente com esse nome na base"

class ErrorSchemaClienteExiste(BaseModel):
    """ Define a mensagem de erro que deve ser apresentada quando um cliente ja existe na base
    """
    message: str="cliente de mesmo nome já salvo na base :/"