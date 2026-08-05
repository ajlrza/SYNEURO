import numpy as np
from neo4j import GraphDatabase
import json, os, random, asyncio, numba, neo4j

URI = os.environ.get("NEO4J_URI")
DATABASE = os.environ.get("NEO4J_DB")
AUTH = (DATABASE, os.environ.get("PW"))

driver = GraphDatabase.driver(URI, auth=AUTH)

driver.verify_connectivity()
driver.verify_connectivity()

driver.execute_query(
    "CREATE DATABASE SYNEURO",
    database_="system" 
)

session = driver.session(database=DATABASE)



session.close()
driver.close()





