# Api-Provenance

![GitHub repo size](https://img.shields.io/github/repo-size/romulolassoares/ApiProv?style=for-the-badge) ![GitHub language count](https://img.shields.io/github/languages/count/romulolassoares/ApiProv?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

---

## Sobre
*API* para efetuar a captura de informações de proveniência de dados, seguindo o modelo [PROV-DM](https://www.w3.org/TR/prov-dm/) e armazenando as informações em um banco de dados de grafos ([NEO4J](https://neo4j.com/)). Codigo desenvolvido para auxiliar a [arquitetura BSPR](https://github.com/BolsaUFJF/bspr) .
Projeto desenvolvido durante um projeto de iniciação científica da Universidade Federal de Juiz de Fora.

---

## Rotas
- */relationships/was-used/post*: cria a relação de used entre uma entidade e uma atividade;
- */relationships/was-generated-by/post*: cria a relação de was genrated by entre uma entidade e uma atividade;
- */relationships/was-associated-with/post*: cria a relação de was associated with entre uma atividade e um agente;
- */relationships/was-attribuited-to/post*: cria a relação de was attribuited to entre uma entidade e um agente;
- */relationships/was-informed-by/post*: cria a relação was informed by entre duas atividades;
- */relationships/was-derived-from/post*: cria a relação was derived from entre duas entidade;
- */relationships/acted-on-behalf/post*: cria a relação acted on behalf entre dois agentes;

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
