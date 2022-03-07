from pydantic import BaseModel, Field
from typing import Optional

class ActivityModel(BaseModel):
   name: str = Field(...)
   provType: str = Field(...)
   start_time: str = Field(...)
   end_time: str = Field(...)
   
   class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            'name': 'Activity Name',
            'provType': 'activity',
            'start_time': 'time1',
            'end_time': 'time2'           
         }
      }
      
class UpdateActivityModel(BaseModel):
   name: Optional[str]
   provType: Optional[str]
   start_time: Optional[str]
   end_time: Optional[str]
   
   class Config:
      arbitrary_types_allowed = True
      schema_extra = {
         "example": {
            "name": "Activity Name",
            "provType": "activity",
            "start_time": "time1",
            "end_time": "time3"           
         }
      }