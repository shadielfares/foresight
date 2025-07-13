# Scraper
## Purpose
The scraper will iterate through an excel sheet `title_person_wiki.xlsx` and leveraging `openpyxl` python package we 
will use `Wikipedia-API` to `extract.py` relevant sections (_potentially Early Life, Career_) sections.

Following the extraction, we would need a seperate script to support an NLP pipeline to take the raw text and normalize
the output. Details in [nlp_pipeline.md](nlp_pipeline.md)

### Related Documenation
1. https://pypi.org/project/openpyxl/
2. https://pypi.org/project/Wikipedia-API/
