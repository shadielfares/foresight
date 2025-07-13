# NLP Pipeline
Post the completion of wikipedia context exctration we need to prepare the information to embed the tuple into 
the [vector database](../db/vector_db/pinecone_graph.py).

## Process
To be completed in order.
1. Role Extraction	Use NER (Named Entity Recognition) + custom entity rules to extract roles (titles).
2. Habit Extraction	Use POS tagging + keyword filtering (e.g. "I practiced for 3 hours") + dependency parsing.
3. Normalize Output	Create a (Role, Habit, Time) tuple structure to be stored in `Pinecone`.

`IMPORTANT`: Refer to [upset_records.py](../db/vector_db/upset_records.py) for an example of format of uploading to the
Pinecone. 

We can take the tuple structure and store it in the Vector DB to be able to find the most similar vector to what the user inputs.
By finding the closest vector and retrieving the semantic components from Pinecone 
(_I assume pinecone implementation provided)_ we complete the first goal in [README.md](../../README.md)!