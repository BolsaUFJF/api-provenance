from fileinput import filename
from fastapi import APIRouter, HTTPException, Depends, status, Body
import json
import src.controller.converterJWT as converterJWT
from src.database.databaseNeo4j import neo4j_driver
import hashlib

router = APIRouter(
   prefix = "/queries",
   tags = ["Queries on Database"],
   responses = {404: {"description": "Not Found"}},
)

@router.get('/when-document-was-sent/{docName}', response_description="Quando o documento x foi enviado")
async def when_document_was_sent(docName: str):
   
   query = (
      "MATCH (:Entity { name: $doc })<-[:WAS_DERIVED_FROM]-(:Entity { provType: 'document-base' })"
      "<-[:USED]-(send:Activity { provType: 'send-document'}) "
      "RETURN send.start_time AS start_time, send.end_time AS end_time"
   )
   
   with neo4j_driver.session() as session:
      result = session.run(query, doc=docName)
      resultData = result.data()[0]
   
   return resultData

@router.get('/when-document-was-converted/{docName}', response_description="Quando o documento x foi convertido")
async def when_document_was_converted(docName: str):
   query = (
      "MATCH (entity:Entity { name: $doc })<-[r:USED]-(activity:Activity { provType: 'convert-document' })  "
      "RETURN activity.start_time AS start_time, activity.end_time AS end_time "
   )
      
   with neo4j_driver.session() as session:
      result = session.run(query, doc=docName).data()
      resultData = result[0]
   return resultData

@router.get('/who-sent-the-document/{docname}', response_description="Quem enviou o documento")
async def who_sent_the_document(docName: str):
   query = (
      "MATCH (:Entity { name: $doc })"
      "<-[:USED]-(:Activity { provType: 'send-document'})-[:WAS_ASSOCIATED_WITH]->(agent:Agent) "
      "RETURN agent.name AS user, agent.data as data"
   )
   with neo4j_driver.session() as session:
      result = session.run(query, doc=docName).data()
      resultData=result[0]
   resultData['data'] = converterJWT.decodeJWT(resultData['data'])
   print(resultData)
   return resultData

@router.get('/get-erros', response_description="Erros capturados")
async def get_erros():
   query = (
      "MATCH (entity:Entity { provType: 'error'}) "
      "RETURN entity "
   )
   with neo4j_driver.session() as session:
      result = session.run(query).data()
      resultData = result
      
   for i in resultData:
      value = i['entity']['data']
      i['entity']['data'] = converterJWT.decodeJWT(value)
   return resultData

# MATCH (n1)-[r:WAS_DERIVED_FROM]->(n2) RETURN n1.name, r, n2

@router.get('/get-document-info', response_description="Informações sobre documentos")
async def get_document_info():
   query = (
      "MATCH (n1)-[r:WAS_DERIVED_FROM]->(n2) "
      "RETURN n1, r, n2 "
   )
   with neo4j_driver.session() as session:
      result = session.run(query).data()
      resultData = result
   dataArray = []
   for i in resultData:
      i['n1']['data'] = converterJWT.decodeJWT(i['n1']['data'])
      i['n2']['data'] = converterJWT.decodeJWT(i['n2']['data'])
      data = {
         "base": i['n1']['data']['base'],
         # "base": hashlib.md5(i['n1']['data']['base'].encode('utf-8')).hexdigest(),
         "relationship": i['r'][1],
         "filename": i['n2']['data']['filename'],
         "format": i['n2']['data']['format'],
         "path": i['n2']['data']['path'],
         "size": i['n2']['data']['size']
      }
      dataArray.append(data)
   return dataArray