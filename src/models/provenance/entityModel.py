from pydantic import BaseModel, Field
from typing import Optional
import src.controller.converterJWT as converterJWT

class EntityModel(BaseModel):
   name: str = Field(...)
   provType: str = Field(...)
   data: dict = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            "name": "Entity Name",
            "provType": "entity-type",
            "data": {} 
         }
      }
   
   def __iter__(self):
      yield 'name', self.name
      yield 'provType', self.provType
      yield 'data', converterJWT.encodeToJWT(self.data)
      
class UpdateEntityModel(BaseModel):
   name: Optional[str]
   provType: Optional[str]
   data: Optional[dict]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            "name": "Entity Name",
            "provType": "entity-type",
            "data": {}      
         }
      }