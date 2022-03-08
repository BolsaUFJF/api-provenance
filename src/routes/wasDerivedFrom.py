from fastapi import APIRouter, HTTPException, Depends, status, Body

from src.database.databaseNeo4j import neo4j_driver

from src.models.provenance.activityModel import ActivityModel
from src.models.provenance.entityModel import EntityModel
from src.models.hybrid.twoEntityModel import TwoEntityModel

router = APIRouter(
   prefix = "/was-derived-from",
   tags = ["Was Derived From Relationship"],
   responses = {404: {"description": "Not Found"}},
)

# ?activity={activity}&entity={entity}
@router.post('/post', response_description="Create Was Derived From")
async def create_was_used(data: TwoEntityModel = Body(...)):
   entity1 = dict(data.entity1)
   entity2 = dict(data.entity2)
   
   print(entity1)
   print(entity2)
   
   query = (
      "MERGE (entity1:Entity { name: $entity1.name, provType: $entity1.provType }) "
      "MERGE (entity2:Entity { name: $entity2.name, provType: $entity2.provType }) "
      "CREATE (entity1)-[:WAS_DERIVED_FROM]->(entity2) "
      "RETURN entity1, entity2"
   )
   
   with neo4j_driver.session() as session:      
      result = session.run(query, entity1=entity1, entity2=entity2)
      resultData = result.data()[0]
      entity2Data = resultData['entity2']
      entity1Data = resultData['entity1']
   
   response = {
      'entity1': entity1Data,
      'entity2': entity2Data
   }
   return response