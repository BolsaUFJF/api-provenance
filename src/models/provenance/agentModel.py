from pydantic import BaseModel, Field
from typing import Optional

import src.controller.converterJWT as converterJWT

class AgentModel(BaseModel):
   name: str = Field(...)
   provType: str = Field(...)
   data: dict = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            "name": "Agent Name",
            "provType": "agent-type",
            "data": {}
         }
      }
   
   def __iter__(self):
      yield 'name', self.name
      yield 'provType', self.provType
      yield 'data', str(converterJWT.encodeToJWT(self.data))
      
class UpdateAgentModel(BaseModel):
   name: Optional[str]
   provType: Optional[str]
   pki: Optional[str]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            "name": "Agent Name",
            "provType": "agent-type",
            "data": {}
         }
      }