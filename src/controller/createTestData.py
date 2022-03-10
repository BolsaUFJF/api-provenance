from src.models.hybrid.activityEntityModel import ActivityEntityModel
from src.models.hybrid.activityAgentModel import ActivityAgentModel
from src.models.hybrid.agentEntityModel import AgentEntityModel
from src.models.hybrid.twoActivityModel import TwoActivityModel
from src.models.hybrid.twoAgentModel import TwoAgentModel
from src.models.hybrid.twoEntityModel import TwoEntityModel

from src.routes.relationships.wasUsedRoutes import create_was_used
from src.routes.relationships.wasGeneratedBy import create_was_generated_by
from src.routes.relationships.wasAssociatedWith import create_was_associated_with
from src.routes.relationships.wasAttribuitedTo import create_was_attribuited_to
from src.routes.relationships.wasInformedBy import create_was_informed_by
from src.routes.relationships.wasDerivedFrom import create_was_derived_from
from src.routes.relationships.actedOnBehalfOf import create_acted_on_behalf_of

activityCreateDocument = {
   "name": "Create Document",
   "provType": "create-document",
   "start_time": "time1",
   "end_time": "time2"
}
activityConvertBase = {
   "name": "Converto to Base",
   "provType": "convert-base",
   "start_time": "time1",
   "end_time": "time2"
}
activitySendDocument = {
   "name": "Send Document",
   "provType": "send-document",
   "start_time": "time1",
   "end_time": "time2"
}

entityDocumentData = {
   "name": "Document Data",
   "provType": "document-data",
   "data": {
      "format": "file format",
      "path": "file location",
      "title": "filename"
   }
}
entityDocumentBase64 = {
   "name": "Document Base 64",
   "provType": "document-base",
   "data": {
      "data_encoded": "base 64 data",
      "mine": "@file/file formart"
   }
}

agentUser = {
   "name": "User",
   "provType": "agent-user",
   "data": {
      "pki": "key",
      "work_for": "company"
   }
}

async def generateData():
   await create_was_generated_by(ActivityEntityModel(activity=activityCreateDocument, entity=entityDocumentData))
   await create_was_associated_with(ActivityAgentModel(activity=activityCreateDocument, agent=agentUser))
   
   await create_was_informed_by(TwoActivityModel(activity1=activityConvertBase, activity2=activityCreateDocument))
   await create_was_used(ActivityEntityModel(activity=activityConvertBase, entity=entityDocumentData))
   await create_was_generated_by(ActivityEntityModel(activity=activityConvertBase, entity=entityDocumentBase64))
   
   await create_was_derived_from(TwoEntityModel(entity1=entityDocumentBase64, entity2=entityDocumentData))
   await create_was_used(ActivityEntityModel(activity=activitySendDocument, entity=entityDocumentBase64))
   await create_was_associated_with(ActivityAgentModel(activity=activitySendDocument, agent=agentUser))
   
