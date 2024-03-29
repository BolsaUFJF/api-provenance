from pydantic import BaseModel, Field
from typing import Optional

from src.models.provenance.entityModel import EntityModel
class TwoEntityModel(BaseModel):
   entity1: EntityModel = Field(...)
   entity2: EntityModel = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'entity1': {
               "name": "Entity Name",
               "provType": "entity-type",
               "data": {} 
            },
            'entity2': {
               "name": "Entity Name",
               "provType": "entity-type",
               "data": {} 
            },         
         }
      }
   
   def __iter__(self):
      yield 'entity1', self.entity1
      yield 'entity2', self.entity2
      
class UpdateTwoEntityModel(BaseModel):
   entity1: Optional[EntityModel]
   entity2: Optional[EntityModel]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'entity1': {
               "name": "Entity Name",
               "provType": "entity-type",
               "data": {} 
            },
            'entity2': {
               "name": "Entity Name",
               "provType": "entity-type",
               "data": {}    
            },         
         }  
      }