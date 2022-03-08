from fastapi import APIRouter, Body

from src.database.databaseNeo4j import neo4j_driver

from src.models.hybrid.agentEntityModel import AgentEntityModel

router = APIRouter(
   prefix = "/was-attribuited-to",
   tags = ["Was Attribuited To Relationship"],
   responses = {404: {"description": "Not Found"}},
)

# ?activity={activity}&entity={entity}
@router.post('/post', response_description="Create Was Attribuited To")
async def create_was_used(data: AgentEntityModel = Body(...)):
   entity = dict(data.entity)
   agent = dict(data.agent)
   
   
   query = (
      "MERGE (agent:Agent { name: $agent.name, provType: $agent.provType }) "
      "MERGE (entity:Entity { name: $entity.name, provType: $entity.provType }) "
      "CREATE (entity)-[:WAS_ATTRIBUITED_TO]->(agent) "
      "RETURN agent, entity"
   )
   
   with neo4j_driver.session() as session:      
      result = session.run(query, agent=agent, entity=entity)
      resultData = result.data()[0]
      agentData = resultData['agent']
      entityData = resultData['entity']
   
   response = {
      'entity': entityData,
      'agent': agentData
   }
   return response