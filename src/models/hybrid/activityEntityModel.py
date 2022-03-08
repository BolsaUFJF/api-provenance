from pydantic import BaseModel, Field
from typing import Optional

from models.provenance.activityModel import ActivityModel
from models.provenance.entityModel import EntityModel

class ActivityEntityModel(BaseModel):
   activity: ActivityModel = Field(...)
   entity: EntityModel = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'activity': {
               'name': 'Activity Name',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time2'
            },
            'entity': {
               "name": "Entity Name",
               "provType": "activity" 
            },         
         }
      }
   
   def __iter__(self):
      yield 'name', self.name
      yield 'provType', self.provType
      yield 'start_time', self.start_time
      yield 'end_time', self.end_time
      
class UpdateActivityModel(BaseModel):
   activity: Optional[ActivityModel]
   entity: Optional[EntityModel]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'activity': {
               'name': 'Activity Name',
               'provType': 'activity',
               'start_time': 'time1',
               'end_time': 'time3'
            },
            'entity': {
               "name": "Entity Name",
               "provType": "activity" 
            },         
         }    
      }