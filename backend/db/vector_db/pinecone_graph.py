import os

from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))\

"""
The remaining details will involve creating a:
    Serverless index to begin semantic search of our tuples:
    (Role, Habit:(List<Strings>), Time:(List<Int>)
    Motivation:
        Be able to perform nearest-neighbor search using the cosine distance metric for 2-dimensional vectors:
        
    Source:
        https://docs.pinecone.io/guides/get-started/quickstart
        
        Will use dense-vectors for semantic search.
"""

index_name = "quickstart"
# Example
pc.create_index(
    name=index_name,
    dimension=2, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)