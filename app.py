from fastapi import FastAPI
from typing import Optional

from src.database.databaseNeo4j import neo4j_driver

from src.routes.wasUsedRoutes import router as was_used_routes

app = FastAPI()

app.include_router(was_used_routes)

@app.get('/', response_description="Root")
def root():
   return {"Status": "Connected"}