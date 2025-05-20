import wikipediaapi

"""
Author: Shadi El-Fares
Purpose: Extract data from Wikipedia pages, put in a link, get text related to the keywords defined.
Dated: 2025-05-19
"""

KEYWORDS = ['early life', 'childhood', 'education', 'background', 'bibliography']

def check_wiki_exists(wiki_wiki, page_title: str) -> bool:
    """Check if a Wikipedia page with the given title exists."""
    return wiki_wiki.page(page_title).exists()

def check_sections_exists(wiki_wiki, page_title: str) -> str:
    """Check if a section within a Wikipedia page with the given page title exists."""

    page_sections = wiki_wiki.page(page_title).sections

    for section in page_sections:
        section_title_lower = section.title.lower()
        for keyword in KEYWORDS:
            if keyword in section_title_lower:
                return section.title

    return None

def get_section_by_title(wiki_wiki, page_title: str) -> str:
    """Retrieval of a relevant section to the KEYWORDS"""

    if check_wiki_exists(wiki_wiki, page_title):
        section_title = check_sections_exists(wiki_wiki, page_title)
        if section_title:
            return wiki_wiki.page(page_title).section_by_title(section_title)

def extract_wiki_text(wiki_wiki, url: str) -> str:
    """Extract text from a Wikipedia page."""
    page_title = url.split("/")[-1]
    return get_section_by_title(wiki_wiki, page_title)

if __name__ == "__main__":
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='ForesightBot/0.0 (admin@foresight.com)', language='en')
    # Dummy link for testing.
    text= extract_wiki_text(wiki_wiki, "https://en.wikipedia.org/wiki/PewDiePie")
    if text:
        print("Extracted Wikipedia text:\n", text)
    else:
        print("No relevant section found or page does not exist.")