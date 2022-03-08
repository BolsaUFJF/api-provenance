from fastapi import APIRouter, HTTPException, Depends, status, Body

from src.database.databaseNeo4j import neo4j_driver

from src.models.hybrid.twoAgentModel import TwoAgentModel

router = APIRouter(
   prefix = "/acted-on-behalf-of",
   tags = ["Acted On Behalf Of Relationship"],
   responses = {404: {"description": "Not Found"}},
)

# ?activity={activity}&entity={entity}
@router.post('/post', response_description="Create Acted On Behalf Of")
async def create_acted_on_behalf_of(data: TwoAgentModel = Body(...)):
   agent1 = dict(data.agent1)
   agent2 = dict(data.agent2)
   
   print(agent1)
   print(agent2)
   
   query = (
      "MERGE (agent1:Agent { name: $agent1.name, provType: $agent1.provType }) "
      "MERGE (agent2:Agent { name: $agent2.name, provType: $agent2.provType }) "
      "CREATE (agent1)-[:ACTED_ON_BEHALF_OF]->(agent2) "
      "RETURN agent1, agent2"
   )
   
   with neo4j_driver.session() as session:      
      result = session.run(query, agent1=agent1, agent2=agent2)
      resultData = result.data()[0]
      agent2Data = resultData['agent2']
      agent1Data = resultData['agent1']
   
   response = {
      'agent1': agent1Data,
      'agent2': agent2Data
   }
   return response