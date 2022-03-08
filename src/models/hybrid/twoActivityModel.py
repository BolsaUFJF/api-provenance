from pydantic import BaseModel, Field
from typing import Optional

from src.models.provenance.agentModel import AgentModel

class Model(BaseModel):
   activity1: AgentModel = Field(...)
   activity2: AgentModel = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'activity1': {
               'name': 'Activity Name 1',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time2'   
            },
            'activity2': {
               'name': 'Activity Name 2',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time2'   
            },         
         }
      }
   
   def __iter__(self):
      yield 'activity1', self.activity1
      yield 'activity2', self.activity2
      
class UpdateModel(BaseModel):
   activity1: Optional[AgentModel]
   activity2: Optional[AgentModel]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'activity1': {
               'name': 'Activity Name 1',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time3'   
            },
            'activity2': {
               'name': 'Activity Name 2',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time3'   
            },         
         }    
      }