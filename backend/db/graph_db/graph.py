import os
from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://a6c4308c.databases.neo4j.io"
username, password = os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD")
AUTH = (username, password)
"""
If the following line outputs:
    None, None 

Doppler is not properly configured.
"""
print(username, password)
with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()