from pinecone import Pinecone



"""
    Instead of (_id, chunk_text, category) it becomes => (Role, Habit:(List<Strings>), Time:(List<Int>)
    
"""

pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

index.upsert(
  vectors=[
    {
      "id": "A",
      "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
      "metadata": {"genre": "comedy", "year": 2020}
    },
    {
      "id": "B",
      "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
      "metadata": {"genre": "documentary", "year": 2019}
    },
    {
      "id": "C",
      "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
      "metadata": {"genre": "comedy", "year": 2019}
    },
    {
      "id": "D",
      "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
      "metadata": {"genre": "drama"}
    }
  ],
  namespace="example-namespace"
)