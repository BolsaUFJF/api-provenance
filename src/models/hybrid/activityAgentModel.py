from pydantic import BaseModel, Field
from typing import Optional

from models.provenance.activityModel import ActivityModel
from models.provenance.entityModel import EntityModel
from models.provenance.agentModel import AgentModel

class ActivityAgentModel(BaseModel):
   activity: ActivityModel = Field(...)
   agent: AgentModel = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'activity': {
               'name': 'Activity Name',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time3'   
            },
            'agent': {
               "name": "Agent Name",
               "provType": "agent-type",
               "data": {}  
            },         
         }
      }
   
   def __iter__(self):
      yield 'activity', self.activity
      yield 'agent', self.agent
      
class UpdateActivityAgentModel(BaseModel):
   activity: Optional[ActivityModel]
   agent: Optional[AgentModel]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
        "example": {
            'agent1': {
               "name": "Agent Name",
               "provType": "agent-type",
               "data": {}  
            },
            'agent2': {
               "name": "Agent Name",
               "provType": "agent-type",
               "data": {} 
            },         
         }  
      }