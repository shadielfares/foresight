from sentence_transformers import SentenceTransformer

"""
Will have to have:
    1. Text-splitter that can handle large texts
    2. Embedding model that can take in text and return embeddings
    3. Similarity function to compare embeddings (for overlap % 10-20% overlap)

TODO: On a different note, I'll need something to generate a role_hint, there has to to be something to label the embeddings with a role hint 
"""

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
#Currently 256, for optimal performance, we should keep the input text length below this value.
max_seq_length = model.max_seq_length 
# The sentences to encode
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]


"""
# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# 3. Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print(similarities)
"""
