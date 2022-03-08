from fastapi import APIRouter, Body

from src.database.databaseNeo4j import neo4j_driver

from src.models.hybrid.activityEntityModel import ActivityEntityModel

router = APIRouter(
   prefix = "/was-used",
   tags = ["Was Used Relationship"],
   responses = {404: {"description": "Not Found"}},
)

# ?activity={activity}&entity={entity}
@router.post('/post', response_description="Create Was Used")
async def create_was_used(data: ActivityEntityModel = Body(...)):
   activity = dict(data.activity)
   entity = dict(data.entity)
   
   query = (
      "MERGE (activity:Activity { name: $activity.name, provType: $activity.provType, start_time: $activity.start_time, end_time: $activity.end_time }) "
      "MERGE (entity:Entity { name: $entity.name, provType: $entity.provType }) "
      "CREATE (activity)-[:USED]->(entity) "
      "RETURN activity, entity"
   )
   
   with neo4j_driver.session() as session:      
      result = session.run(query, activity=activity, entity=entity)
      resultData = result.data()[0]
      activityData = resultData['activity']
      entityData = resultData['entity']
   
   response = {
      'activity': activityData,
      'entity': entityData
   }
   return response

# @router.put('/update', response_description="Update Was Used")
# def update_was_used(data: ActivityEntityModel = Body(...)):
#    activity = dict(data.activity)
#    entity = dict(data.entity)
   
#    searchRelationship = (
#       "MATCH (activity:Activity) WHERE activity.name = $activity.name "
#       "MATCH (entity:Entity) WHERE entity.name = $entity.name "
#       "MATCH (activity)-[rel:USED]->(entity) "
#       "RETURN rel"
#    )
   
#    query = (
#       "MATCH (activity:Activity) WHERE activity.name = $activity.name "
#       "MATCH (entity:Entity) WHERE entity.name = $entity.name "
#       "MATCH (activity)-[rel:USED]->(entity) "
#       "SET activity.end_time = $activity.end_time "
#       "RETURN rel, activity, entity"
#    )
   
#    with neo4j_driver.session() as session:
#       checkRelationship = session.run(query=searchRelationship, activity=activity, entity=entity)
#       if checkRelationship.data():
#          result = session.run(query, activity=activity, entity=entity)
#          resultData = result.data()[0]
   
#    return resultData