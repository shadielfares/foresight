import json
import requests
import os

API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"

token = os.getenv("HF_SECRET")  # Ensure the environment variable is set
HP_TOKEN = token
headers = {"Authorization": f"Bearer {HP_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def calculate_relatability_score(article, habits):
    payload = {
        "inputs": {
            "source_sentence": article,
            "sentences": habits
        }
    }
    response = query(payload)

    relatability_score = 0
    for habit_score in response:
        relatability_score += habit_score

    return relatability_score / len(habits)

def rank_relatability(people, articles, habits):

    relatability_scores = []

    for index in range(len(articles)):

        score = calculate_relatability_score(articles[index], habits)
        relatability_scores.append([score, people[index]])

    relatability_scores.sort(reverse=True)

    return relatability_scores[0:3]

print(rank_relatability(people, [article1, article2, article3], ["Playing video games", "Live streaming", "Making videos"]))