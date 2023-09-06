from schemas.cliente import ClienteSchema, ClienteViewSchema, apresenta_cliente
from schemas.error import ErrorSchema, ErrorSchemaCliente, ErrorSchemaGuia, ErrorSchemaLugar, ErrorSchemaLugarExiste, ErrorSchemaClienteExiste, ErrorSchemaGuiaExiste, ErrorSchemaPasseio
from schemas.lugar import LugarSchema, LugarViewSchema, apresenta_lugar
from schemas.guia import GuiaSchema, GuiaViewSchema, apresenta_guia
from schemas.passeio import PasseioSchema, PasseioViewSchema, PasseioGetSchema, PasseioDelSchema, apresenta_passeio
from schemas.comentario import ComentarioSchema, ComentarioViewSchema, ComentarioDelSchema, apresenta_comentario