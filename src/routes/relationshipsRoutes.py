# from fastapi import APIRouter, HTTPException, Depends, status

# from src.database.databaseNeo4j import neo4j_driver

# router = APIRouter(
#    prefix = "/relationship",
#    tags = ["Relationship Router"],
#    responses = {404: {"description": "Not Found"}},
# )

# # ?activity={activity}&entity={entity}
# @router.post('/was-used', response_description="Was Used")
# async def was_used():
#    activity = {
#       'name': 'Create User',
#       'type': 'activity',
#       'start-time': 'time1',
#       'end-time': 'time2'
#    }
   
#    entity = {
#       'name': 'User',
#       'type': 'entity-user',
#    }
   
#    searchRelationship = (
#       "MATCH (activity:Activity) WHERE activity.name = $activity RETURN activity "
#       "MATCH (entity:Entity) WHERE entity.name = $entity RETURN entity "
#       "MATCH (activity)-[relationship]->(entity) WHERE relationship = USED "
#       "RETURN relationship"
#    )
   
#    query = (
#       "MERGE (activity:Activity { name: $activity.name, type: $activity.type, start_time: $activity.start_time, end_time: $activity.end_time }) "
#       "MERGE (entity:Entity { name: $entity }) "
#       "CREATE (activity)-[:USED]->(entity) "
#       "RETURN activity, entity"
#    )
   
#    with neo4j_driver.session() as session:      
#       result = session.run(query, activity=activity, entity=entity['name'])
#       resultData = result.data()[0]
#       activityData = resultData['activity']
#       entityData = resultData['entity']
   
#    response = {
#       'activity': activityData,
#       'entity': entityData
#    }
#    return response