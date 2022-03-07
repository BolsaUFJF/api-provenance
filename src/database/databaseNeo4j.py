from neo4j import GraphDatabase
import os
from dotenv import load_dotenv, find_dotenv

env_loc = find_dotenv('.env')
load_dotenv(env_loc)

uri=os.getenv("uri")
user=os.getenv("user")
pwd=os.getenv("pwd")

neo4j_driver = GraphDatabase.driver(uri=uri, auth=(user, pwd))