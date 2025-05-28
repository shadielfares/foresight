import requests
import os
import logging

from sheet_traversal import extract_name_col, extract_articles_col, SHEET
from extract import extract_wiki_text, WIKI_WIKI

"""
Author: Aiden Sanvido, Shadi El-Fares
Purpose:
    Given an array of strings, rank the well-known individuals across a variety of industries to what matches them the most.
    Currently utilizes a sentence transformer.
Note: Ignore NotOpenSSLWarning
Dated: 2025-05-27
"""

logging = logging.getLogger(__name__)

API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"

token = os.getenv("HF_SECRET")  # Ensure the environment variable is set
HP_TOKEN = token
headers = {"Authorization": f"Bearer {HP_TOKEN}"}

def query(payload) -> list[float]:
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Query failed: {e}")
        return [0.0] * len(payload["inputs"]["sentences"])  # fallback

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

def rank_relatability(people: list[str], articles: list[str], habits: list[str]) -> list[list[int]]:

    relatability_scores = []

    for index in range(len(articles)):

        score = calculate_relatability_score(articles[index], habits)
        relatability_scores.append([score, people[index]])

    relatability_scores.sort(reverse=True)

    return [relatability_scores[0:3], relatability_scores[-3:]]

if __name__ == "__main__":
    people, articles = extract_name_col(SHEET, []), extract_articles_col(SHEET, [])
    blocks = []
    for url_x in articles:
        logging.info(f"Currently Processing: {url_x}")
        blocks.append(str(extract_wiki_text(WIKI_WIKI, url_x)))

    print(rank_relatability(people, blocks, ["Smoking", "Drug ingesting", "Dancing"]))