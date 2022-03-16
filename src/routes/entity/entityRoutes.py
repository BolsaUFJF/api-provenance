from fastapi import APIRouter, Body

from src.database.databaseNeo4j import neo4j_driver

from src.models.hybrid.activityEntityModel import ActivityEntityModel

router = APIRouter(
   prefix = "/entity",
   tags = ["Entity Routes"],
   responses = {404: {"description": "Not Found"}},
)

@router.get('/get-last', response_description="Get Last Entity")
async def get_last_entity():

   
   query = (
      "MATCH (n:Entity) "
      "WHERE n.provType = 'document-base' "
      "RETURN n "
      "ORDER BY n.created_at "
   )
   
   with neo4j_driver.session() as session:      
      result = session.run(query)
      resultData = result.data()[-1]
   
   return resultData