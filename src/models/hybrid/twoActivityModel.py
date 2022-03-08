from pydantic import BaseModel, Field
from typing import Optional

from src.models.provenance.activityModel import ActivityModel

class TwoActivityModel(BaseModel):
   activity1: ActivityModel = Field(...)
   activity2: ActivityModel = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'activity1': {
               'name': 'Activity Name',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time2'   
            },
            'activity2': {
               'name': 'Activity Name',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time2'   
            },         
         }
      }
   
   def __iter__(self):
      yield 'activity1', self.activity1
      yield 'activity2', self.activity2
      
class UpdateTwoActivityModel(BaseModel):
   activity1: Optional[ActivityModel]
   activity2: Optional[ActivityModel]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'activity1': {
               'name': 'Activity Name',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time3'   
            },
            'activity2': {
               'name': 'Activity Name',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time3'   
            },         
         }    
      }