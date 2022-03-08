from pydantic import BaseModel, Field
from typing import Optional

class EntityModel(BaseModel):
   name: str = Field(...)
   provType: str = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            "name": "Entity Name",
            "provType": "entity-type"    
         }
      }
   
   def __iter__(self):
      yield 'name', self.name
      yield 'provType', self.provType
      
class UpdateEntityModel(BaseModel):
   name: Optional[str]
   provType: Optional[str]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'name': 'Entity Name',
            'provType': 'entity-type'       
         }
      }