from fastapi import FastAPI
from typing import Optional

from src.database.databaseNeo4j import neo4j_driver

from src.routes.wasUsedRoutes import router as was_used_routes
from src.routes.wasGeneratedBy import router as was_generated_by_routes
from src.routes.wasAssociatedWith import router as was_associated_with_routes
from src.routes.wasAttribuitedTo import router as was_attribuited_to_routes

app = FastAPI()

app.include_router(was_used_routes)
app.include_router(was_generated_by_routes)
app.include_router(was_associated_with_routes)
app.include_router(was_attribuited_to_routes)

@app.get('/', response_description="Root")
def root():
   return {"Status": "Connected"}