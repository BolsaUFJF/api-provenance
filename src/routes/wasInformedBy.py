from fastapi import APIRouter, HTTPException, Depends, status, Body

from src.database.databaseNeo4j import neo4j_driver

from src.models.provenance.activityModel import ActivityModel
from src.models.provenance.entityModel import EntityModel
from src.models.hybrid.twoActivityModel import TwoActivityModel

router = APIRouter(
   prefix = "/was-informed-by",
   tags = ["Was Informed By Relationship"],
   responses = {404: {"description": "Not Found"}},
)

# ?activity={activity}&entity={entity}
@router.post('/post', response_description="Create Was Informed By")
async def create_was_used(data: TwoActivityModel = Body(...)):
   activity1 = dict(data.activity1)
   activity2 = dict(data.activity2)
   
   print(activity1)
   print(activity2)
   
   query = (
      "MERGE (activity1:Activity { name: $activity1.name, provType: $activity1.provType, start_time: $activity1.start_time, end_time: $activity1.end_time }) "
      "MERGE (activity2:Activity { name: $activity2.name, provType: $activity2.provType, start_time: $activity2.start_time, end_time: $activity2.end_time }) "
      "CREATE (activity1)-[:WAS_INFORMED_BY]->(activity2) "
      "RETURN activity1, activity2"
   )
   
   with neo4j_driver.session() as session:      
      result = session.run(query, activity1=activity1, activity2=activity2)
      resultData = result.data()[0]
      activity2Data = resultData['activity2']
      activity1Data = resultData['activity1']
   
   response = {
      'activity1': activity1Data,
      'activity2': activity2Data
   }
   return response