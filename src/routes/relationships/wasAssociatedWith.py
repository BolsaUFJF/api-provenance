from fastapi import APIRouter, HTTPException, Depends, status, Body

from src.database.databaseNeo4j import neo4j_driver

from src.models.hybrid.activityAgentModel import ActivityAgentModel

router = APIRouter(
   prefix = "/was-associated-with",
   tags = ["Was Associated With Relationship"],
   responses = {404: {"description": "Not Found"}},
)

@router.post('/post', response_description="Create Was Associated To")
async def create_was_associated_with(data: ActivityAgentModel = Body(...)):
   activity = dict(data.activity)
   agent = dict(data.agent)
   
   query = (
      "MERGE (activity:Activity { name: $activity.name, provType: $activity.provType, start_time: $activity.start_time, end_time: $activity.end_time }) "
      "MERGE (agent:Agent { name: $agent.name, provType: $agent.provType }) "
      "CREATE (activity)-[:WAS_ASSOCIATED_WITH]->(agent) "
      "RETURN activity, agent"
   )
   
   with neo4j_driver.session() as session:      
      result = session.run(query, activity=activity, agent=agent)
      resultData = result.data()[0]
      activityData = resultData['activity']
      agentData = resultData['agent']
   
   response = {
      'activity': activityData,
      'agent': agentData
   }
   return response
