from pydantic import BaseModel, Field
from typing import Optional

from src.models.provenance.agentModel import AgentModel

class TwoAgentModel(BaseModel):
   agent1: AgentModel = Field(...)
   agent2: AgentModel = Field(...)
   
   class Config:
      allow_population_by_field_name = True
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
   
   def __iter__(self):
      yield 'agent1', self.agent1
      yield 'agent2', self.agent2
      
class UpdateTwoAgentModel(BaseModel):
   agent1: Optional[AgentModel]
   agent2: Optional[AgentModel]
   
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