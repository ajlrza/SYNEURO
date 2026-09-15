import numpy as np
from neo4j import GraphDatabase
import json, os, random, asyncio, numba, neo4j

URI = os.environ.get("NEO4J_URI")
DATABASE = os.environ.get("NEO4J_DB")
AUTH = (DATABASE, os.environ.get("PW"))
DRIVER = GraphDatabase.driver(URI, auth=AUTH)

memory_to_store: dict[str, any] = {}

DRIVER = GraphDatabase.driver(URI, auth=AUTH)

DRIVER.verify_connectivity()

DRIVER.execute_query(
    "CREATE DATABASE SYNEURO",
    database_="system" 
)

SESSION = DRIVER.session(database=DATABASE)



SESSION.close()
DRIVER.close()





