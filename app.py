from fastapi import FastAPI
import json

from src.routes.relationshipsRoutes import router as relationships_routes
from src.routes.entity.entityRoutes import router as entity_routes

from src.database.databaseNeo4j import neo4j_driver
import src.controller.converterJWT as converterJWT

from src.controller.createTestData import generateData
app = FastAPI()

app.include_router(relationships_routes)
app.include_router(entity_routes)

@app.get('/', response_description="Root")
def root():
   return {
      "Status": "Connected",
      "status_code": "200",
      "routes": {
         "relationships": {
            "posts": {
               "was_used": "/relationships/was-used/post",
               "was_generated_by": "/relationships/was-generated-by/post",
               "was_associated_with": "/relationships/was-associated-with/post",
               "was_attribuited_to": "/relationships/was-attribuited-to/post",
               "was_informed_by": "/relationships/was-informed-by/post",
               "was_derived_from": "/relationships/was-derived-from/post",
               "acted_on_behalf": "/relationships/acted-on-behalf/post"
            }
         }
      }
   }
   
@app.get('/test', response_description="Test")
async def test():
   await generateData()
   return "hello"


@app.get('/get-all', response_description="Get All")
async def get_all():
   query = (
      "MATCH (n1)-[r]->(n2) "
      "RETURN r, n1, n2 "
   )
   
   with neo4j_driver.session() as session:      
      result = session.run(query)
      resultData = result.data()
      
   result = dict()

   for x, i in enumerate(resultData):
      data = {
         "node1": str(converterJWT.encodeToJWT(i["r"][0])),
         "node2": str(converterJWT.encodeToJWT(i["r"][2])),
         "relationship": i["r"][1]
      }
      result.update({x: data})
   
   return result