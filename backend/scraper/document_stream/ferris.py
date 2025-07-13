from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time, re, requests, os
from urllib.parse import urlparse

FERRIS_TRANSCRIPTS_URL = "https://tim.blog/2018/09/20/all-transcripts-from-the-tim-ferriss-show/"
LOAD_TIMEOUT = 10 # seconds
driver = webdriver.Chrome()


def get_old_links(): #Gets PDF links from the old format
    driver.get(FERRIS_TRANSCRIPTS_URL)
    time.sleep(LOAD_TIMEOUT)  # Wait for the page to load completely
    elements = driver.find_elements("tag name", "a")
    old_pattern = r"https:\/\/tim\.blog\/wp-content\/uploads\/\d{4}\/\d{2}\/[a-zA-Z0-9-]+\/\#conten:\/\/tim\.blog\/wp-content\/uploads\/\d{4}\/\d{2}\/[a-zA-Z0-9-]+\.pdf"
    old_links = [element.get_attribute("href") for element in elements if element.get_attribute("href") and re.match(old_pattern, element.get_attribute("href"))]
    return old_links

def download_pdf(links, output_dir="transcripts"):
    os.makedirs(output_dir, exist_ok=True)
    for url in links:
        filename = os.path.join(output_dir, url.split("/")[-1])
        if not os.path.exists(filename):
            print(f"Downloading {filename}...")
            with requests.get(url, stream=True) as r:
                with open(filename, "wb") as file:
                    file.write(r.content)
                print(f"Downloaded {filename}")
        else:
            print(f"{filename} already exists, skipping download.")

def get_new_links():  # Gets links from the new format
    driver.get(FERRIS_TRANSCRIPTS_URL)
    time.sleep(LOAD_TIMEOUT)  # Wait for the page to load completely
    elements = driver.find_elements("tag name", "a")
    new_pattern = r"https:\/\/tim\.blog\/\d{4}\/\d{2}\/\d{2}\/[a-zA-Z0-9-]+\/\#content"
    new_links = [element.get_attribute("href") for element in elements if element.get_attribute("href") and re.match(new_pattern, element.get_attribute("href"))]
    return new_links

def get_new_links_modified():  # Gets links from the new format with modified URL
    driver.get(FERRIS_TRANSCRIPTS_URL)
    time.sleep(LOAD_TIMEOUT)  # Wait for the page to load completely
    elements = driver.find_elements("tag name", "a")
    new_pattern = r"https:\/\/tim\.blog\/\d{4}\/\d{2}\/\d{2}\/[a-zA-Z0-9-]+\/"
    new_links = [element.get_attribute("href") for element in elements if element.get_attribute("href") and re.match(new_pattern, element.get_attribute("href"))]
    return new_links

def extract_text_from_link(url):
    driver.get(url)
    try:
        WebDriverWait(driver, LOAD_TIMEOUT).until(
            EC.presence_of_element_located((By.CLASS_NAME, "entry-content"))
        )
    except:
        print(f"Error: Could not load the page {url}.")
        return []

    # 2. Find all <p> and the #jp-relatedposts inside that div
    entry_div = driver.find_element("class name", "entry-content")
    children = entry_div.find_elements("xpath", "./*")

    results = []
    for child in children:
        if child.get_attribute("id") == "jp-relatedposts":
            break
        if child.tag_name == "p":
            results.append(child.text.strip())

    return results

def save_to_txt(paragraphs, filename="output.txt", output_dir="manual_transcripts"):
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        for para in paragraphs:
            f.write(para + "\n\n")  # double newline for paragraph spacing
        print(f"✅ Saved {len(paragraphs)} paragraphs to {full_path}")

def get_filename_from_url(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/")  # remove leading/trailing slashes

    if url.endswith(".pdf"):
        # Old format — use the last part of the path
        return path.split("/")[-1]

    slug = path.split("/")[-1]
    if not slug:
        slug = path.split("/")[-2]
        
    return f"{slug}.txt"

def download_and_extract_text(links, output_dir="transcripts"):
    os.makedirs(output_dir, exist_ok=True)
    for url in links:
        filename = get_filename_from_url(url)
        if not os.path.exists(filename):
            print(f"Extracting text from {url}...")
            paragraphs = extract_text_from_link(url)
            save_to_txt(paragraphs, filename)
        else:
            print(f"{filename} already exists, skipping extraction.")

# links = ["https://tim.blog/2022/03/24/mark-zuckerberg-transcript/"]

input("Press Enter to start downloading PDFs...")
links_new = get_new_links()
links_new_modified = get_new_links_modified()
# it worked as a single link but when i have more than one link it doesn't work
combined_links = links_new + links_new_modified 
#print(f"Found {len(links_new_modified)} new links.")
#print(links_new_modified)
download_and_extract_text(combined_links)
# download_pdf(old_links)
driver.quit()
