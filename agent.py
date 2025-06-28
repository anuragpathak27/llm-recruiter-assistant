from search import search_candidates
from scoring import score_fit
from outreach import generate_messages
from scrape_profile import extract_profile_data
from utils import store_data

class LinkedInAgent:
    def search_linkedin(self, job_description):
        # Step 1: Get LinkedIn URLs
        basic_profiles = search_candidates(job_description)

        # Step 2: Enrich each profile with full scraping
        enriched_profiles = []
        for profile in basic_profiles:
            print(f"Scraping: {profile['linkedin_url']}")
            try:
                scraped = extract_profile_data(profile["linkedin_url"])
                enriched = {**profile, **scraped}
                enriched_profiles.append(enriched)
            except Exception as e:
                print(f"Failed to scrape {profile['linkedin_url']}: {e}")
        return enriched_profiles

    def score_candidates(self, candidates, job_description):
        return score_fit(candidates, job_description)

    def generate_outreach(self, scored_candidates, job_description, job_id="default"):
        messages = generate_messages(scored_candidates, job_description)
        store_data(scored_candidates, messages, job_id)
        return messages
