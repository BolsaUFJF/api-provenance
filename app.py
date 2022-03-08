from fastapi import FastAPI

from src.routes.relationshipsRoutes import router as relationships_routes

app = FastAPI()

app.include_router(relationships_routes)

@app.get('/', response_description="Root")
def root():
   return {
      "Status": "Connected",
      "status_code": "200",
      "routes": {
         "relationships": {
            "posts": {
               "was_used": "/relationships/was-used/post",
               "was_generated_by": "/relationships/was-generated-by/post",
               "was_associated_with": "/relationships/was-associated-with/post",
               "was_attribuited_to": "/relationships/was-attribuited-to/post",
               "was_informed_by": "/relationships/was-informed-by/post",
               "was_derived_from": "/relationships/was-derived-from/post",
               "acted_on_behalf": "/relationships/acted-on-behalf/post"
            }
         }
      }
   }