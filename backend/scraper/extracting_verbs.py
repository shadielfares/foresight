import spacy
from spacy.matcher import Matcher

with open('./data/wikipedia.txt', 'r') as file:
    text = file.read().replace('\n\n', ' ').replace('\n', ' ')

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# Search for action phrases
matcher = Matcher(nlp.vocab)
pattern = [
    {"POS": "VERB"},
    {"POS": "DET", "OP": "?"},
    {"POS": "NOUN", "OP": "+"}
]

matcher.add("VERB_PHRASE", [pattern])
matches = matcher(doc)

sentence_matches = {}

for match_id, start, end in matches:
    span = doc[start:end]
    sent = span.sent

    sent_key = (sent.start, sent.end)

    # Collect the longest match per sentence
    if sent_key not in sentence_matches or len(span) > len(sentence_matches[sent_key]):
        sentence_matches[sent_key] = span

for span in sentence_matches.values():
    print(f"Matched phrase: {span.text}")
    print(f"Sentence: {span.sent.text}\n")