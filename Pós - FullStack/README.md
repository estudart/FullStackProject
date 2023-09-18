# Minha API

Este projeto faz parte da entrega do meu primeiro MVP para a a pós-graduação em FullStack pela PUC-RIO.

A ideia do projeto é conectar pessoas interessadas em passeios e guias turisticos especializados, e dessa forma, decentralizar o turismo
e facilitar o agendamento de passeios para os mais diversos locais.

Nessa etapa, deixo um exemplo do meu código para a execução da API, ela roda em um localhost e contém os dados em um banco de dados SQLite,
banco de dados esses que é bem simples de ser analisado e bem leve para se ter em sua máquina.

Dentre as diversas possibilidades da API, algumas delas são: cadastro de novos clientes na base, cadastro de guias, adicionar comentários e até
mesmo cadastrar novos lugares para ir.

---
## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
