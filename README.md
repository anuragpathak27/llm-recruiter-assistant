#### LLM Recruiter Assistant
**LLM-powered AI Agent for Scoring LinkedIn Profiles Based on Job Fit**
This project builds a recruitment assistant that scrapes LinkedIn profiles, evaluates candidate fit based on a job description, and generates personalized outreach messages using LLMs. It helps automate the early-stage sourcing and triage process for tech hiring.
## Features
•	Scrapes public LinkedIn profiles using `undetected_chromedriver`
•	Calculates a custom Fit Score based on: Education, Work trajectory, Company prestige, Skills, Location
•	Uses LLMs (via OpenAI) to draft personalized outreach messages
•	JSON-based architecture for easy logging and extension
## How It Works
1.	 Input a job description and a list of LinkedIn profile URLs.
2.	 The agent scrapes and parses key candidate data.
3.	 Each profile is scored based on a weighted rubric.
4.	 A personalized message is generated for each candidate.

## Project Structure
.
├── main.py                  # Main driver script
├── scraper.py               # LinkedIn scraping logic
├── scorer.py                # Fit score computation logic
├── message_generator.py     # OpenAI-based message generator
├── candidates.json          # Sample scraped data
├── job_description.txt      # Sample job description
└── README.md

Setup Instructions
1. Clone the Repository

git clone https://github.com/your-username/llm-candidate-ranker.git

2. Install Dependencies

python -m venv env
env\Scripts\activate
pip install -r requirements.txt

3. Set Environment Variables

huggingface_api_key
serpapi_api_key
linkedin_username
linkedin_account_password

## Run the Project

python main.py

Customize the list of LinkedIn URLs and the job description in `main.py`.
## Scoring Rubric (Weights)
Factor	Weight	Criteria Example
Education	20%	MIT, Stanford, CMU, UIUC
Trajectory	20%	≥ 2 companies, clear promotion history
Company	15%	Worked at Google, OpenAI, etc.
Skills	25%	"ML", "LLM", "AI" in headline
Location	10%	Based in/near Mountain View, CA
Tenure	10%	Placeholder (can be extended via timeline)

📌 Limitations
•	⚠️ Limited to publicly viewable LinkedIn data
•	⚠️ No persistent DB; uses in-memory structures for demo
🤝 Contributions
Feel free to fork, extend scoring logic, or integrate additional LLM providers (Claude, Gemini, Groq, etc.).
📄 License
MIT License

---
## Anurag Pathak
