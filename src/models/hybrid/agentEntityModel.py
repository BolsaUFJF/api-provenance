from pydantic import BaseModel, Field
from typing import Optional

from src.models.provenance.activityModel import ActivityModel
from src.models.provenance.entityModel import EntityModel
from src.models.provenance.agentModel import AgentModel

class AgentEntityModel(BaseModel):
   agent: AgentModel = Field(...)
   entity: EntityModel = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'agent': {
               "name": "Agent Name",
               "provType": "agent-type",
            },
            'entity': {
               "name": "Entity Name",
               "provType": "entity-type" 
            },         
         }
      }
   
   def __iter__(self):
      yield 'agent', self.agent
      yield 'entity', self.entity
      
class UpdateAgentEntityModel(BaseModel):
   agent: Optional[AgentModel]
   entity: Optional[EntityModel]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'agent': {
               "name": "Agent Name",
               "provType": "agent-type",
            },
            'entity': {
               "name": "Entity Name",
               "provType": "entity-type" 
            },         
         }
      }