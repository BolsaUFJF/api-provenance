from pydantic import BaseModel, Field
from typing import Optional

from src.models.provenance.activityModel import ActivityModel
from src.models.provenance.entityModel import EntityModel

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
               "provType": "entity-type" 
            },         
         }
      }
      
   # def __init__(self, activity: ActivityModel, entity: EntityModel):
   #    self.activity = activity
   #    self.entity = entity
   
   def __iter__(self):
      yield 'activity', self.activity
      yield 'entity', self.entity
      
class UpdateActivityEntityModel(BaseModel):
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
               "provType": "entity-type" 
            },         
         }    
      }