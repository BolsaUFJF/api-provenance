from fastapi import FastAPI
from typing import Optional

from src.database.databaseNeo4j import neo4j_driver

app = FastAPI()

@app.get('/', response_description="Root")
def root():
   return {"Status": "Connected"}