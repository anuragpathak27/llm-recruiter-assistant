import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

def search_candidates(job_description):
    query = f'site:linkedin.com/in "ML Engineer" "LLM" "CodeGen"'
    params = {
        "q": query,
        "engine": "google",
        "api_key": "c0dbb38fa842d277c23119e7d840869081408ce953dd8b6d3beda4ffa10729cb"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    links = [res['link'] for res in results.get("organic_results", [])]
    
    candidates = []
    for link in links:
        candidates.append({
            "name": "Unknown",  # Update with parser if needed
            "linkedin_url": link,
            "headline": "N/A"
        })
    return candidates
