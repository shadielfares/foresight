# Models

Alright... I know its kind of confusing with the idea of a `vector_db` and `graph_db`.

The first model to discuss is a `sentence_transformer`, we may use a model on Hugging Face (_HF_)
known as [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).

 `IMPORTANT`: We don't a sentence-transformer if our NLP pipeline can get the job done reliabily enough.
 
We don't actually need any models given that we pivotted to leveraging a `vector_db` and `graph_db`, the query we do 
is the mechanism that will actually `search` for matches instead of having a traditional model be trained on it.

Its weird, but I mean it makes sense to me and it seems like an alternative way of doing it.

We coulld consider actually implementing a model later if we find that this solution is bad.