# Api-Provenance

![GitHub repo size](https://img.shields.io/github/repo-size/romulolassoares/ApiProv?style=for-the-badge) ![GitHub language count](https://img.shields.io/github/languages/count/romulolassoares/ApiProv?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

---

## Sobre
*API* para efetuar a captura de informações de proveniência de dados, seguindo o modelo [PROV-DM](https://www.w3.org/TR/prov-dm/) e armazenando as informações em um banco de dados de grafos ([NEO4J](https://neo4j.com/)). Codigo desenvolvido para auxiliar a [arquitetura BSPR](https://github.com/BolsaUFJF/bspr) .
Projeto desenvolvido durante um projeto de iniciação científica da Universidade Federal de Juiz de Fora.

---

## Schemas
Data schemas presentes na *api*.

- **ActivityModel**:
   ``` json
   "activity": {
      "name": "Activity Name",
      "provType": "activity",
      "start_time": "time1",
      "end_time": "time2"
   }
   ```
- **EntityModel**:
   ``` json
   "entity": {
      "name": "Entity Name",
      "provType": "entity-type",
      "data": {}
   }
   ```
- **AgentModel**:
   ``` json
   "agent": {
      "name": "Agent Name",
      "provType": "agent-type",
      "data": {}
   }
   ```
- **ActivityAgentModel**:
   ``` json
   {
      "activity": {
         "name": "Activity Name",
         "provType": "activity",
         "start_time": "time1",
         "end_time": "time2"
      },
      "agent": {
         "name": "Agent Name",
         "provType": "agent-type",
         "data": {}
      }
   }
   ```
- **ActivityEntityModel**:
   ``` json
   {
      "activity": {
         "name": "Activity Name",
         "provType": "activity",
         "start_time": "time1",
         "end_time": "time2"
      },
      "entity": {
         "name": "Entity Name",
         "provType": "entity-type",
         "data": {}
      }
   }
   ```
- **AgentEntityModel**:
   ``` json
   {
      "agent": {
         "name": "Agent Name",
         "provType": "agent-type",
         "data": {}
      },
      "entity": {
         "name": "Entity Name",
         "provType": "entity-type",
         "data": {}
      }
   }
   ```
- **TwoActivityModel**:
   ``` json
   {
      "activity1": {
         "name": "Activity Name",
         "provType": "activity",
         "start_time": "time1",
         "end_time": "time2"
      },
      "activity2": {
         "name": "Activity Name",
         "provType": "activity",
         "start_time": "time1",
         "end_time": "time2"
      }
   }
   ```
- **TwoAgentModel**:
   ``` json
   {
      "agent1": {
         "name": "Agent Name",
         "provType": "agent-type",
         "data": {}
      },
      "agent2": {
         "name": "Agent Name",
         "provType": "agent-type",
         "data": {}
      }
   }
   ```
- **TwoEntityModel**:
   ``` json
   {
      "entity1": {
         "name": "Entity Name",
         "provType": "entity-type",
         "data": {}
      },
      "entity2": {
         "name": "Entity Name",
         "provType": "entity-type",
         "data": {}
      }
   }
   ```



## Rotas
Rotas presentes na *api*.
- Relationships Routes: rotas referentes as relações do modelo PROV-DM
  - */relationships/was-used/post*: cria a relação de used entre uma entidade e uma atividade;
  - */relationships/was-generated-by/post*: cria a relação de was genrated by entre uma entidade e uma atividade;
  - */relationships/was-associated-with/post*: cria a relação de was associated with entre uma atividade e um agente;
  - */relationships/was-attribuited-to/post*: cria a relação de was attribuited to entre uma entidade e um agente;
  - */relationships/was-informed-by/post*: cria a relação was informed by entre duas atividades;
  - */relationships/was-derived-from/post*: cria a relação was derived from entre duas entidade;
  - */relationships/acted-on-behalf/post*: cria a relação acted on behalf entre dois agentes;
- Entity Routes: rotas referentes as entidades:
  - */entity/get-last*: busca a ultima entidade inserida no banco de dados;
  - */entity/get-by-name/{name}*: busca uma entidade informando o nome (*name*) da mesma;
- Queries on Database: rotas para efetuar consultas espeficas no banco de dados:
  - */queries/when-document-was-sent/{docName}*: rotas para saber quando um documento, passando o nome do mesmo (*docName*), foi enviado;
  - */queries/when-document-was-convert/{docName}*: rota para saber quando um documento, passando o nome do mesmo (*docName*), foi convertido;
  - */queries/who-sent-the-document/{docName}*: rota para saber quem enviou um documento, passando o nome do mesmo (*docName*);
  - */queries/get-erros*: rota para consultar todos os erros presentes no bando de dados;
  - */queries/get-document-info*: rota para consultar as informações de todos os documentos;
  - */queries/get-all-agents*: rota para consultar todos os agentes no banco de dados;
---

## Pré-requisitos
Iniciar uma instância do Neo4j de forma local na sua máquina ou utilizando o Neo4j AuraDB online.

---

## Execução
Inicializar o banco de dados Neo4j primeiramente.
``` shell
# Install the requirements:
pip install -r requirements.txt
# Start the service:
uvicorn app:app --reload --port 3333
```

Para visualizar as rotas da *api* acesse [http://localhost:3333/docs](http://localhost:3333/docs)

[⬆ Voltar ao topo](#api-provenance)<br>
