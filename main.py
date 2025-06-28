from agent import LinkedInAgent

agent = LinkedInAgent()

job_description = """
Windsurf (formerly Codeium) is a Forbes AI 50 company focused on transforming developer productivity using AI. With $243M in funding and a global user base of hundreds of thousands, our tools power autocomplete, code chat, and full IDE experiences using proprietary LLMs.

Role: Software Engineer – ML Research  
Location: Onsite, Mountain View, CA

Responsibilities:
- Train and fine-tune large language models (LLMs) for developer productivity.
- Run ablation studies and design impactful ML experiments.
- Turn research insights into scalable product features.
- Collaborate in ML reading groups and cross-functional teams.

Requirements:
- 2+ years in software engineering with fast growth or promotions.
- Experience training large production-grade neural networks.
- Strong engineering and system design skills.
- High GPA from a top CS university (MIT, Stanford, CMU, UIUC, etc.).
- Familiarity with tools like Copilot, ChatGPT, or Windsurf preferred.
- Strong interest in code generation and applied ML research.
"""

candidates = agent.search_linkedin(job_description)
scored = agent.score_candidates(candidates, job_description)
messages = agent.generate_outreach(scored[:5], job_description)

print(messages)