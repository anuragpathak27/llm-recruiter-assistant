def score_fit(candidates, job_description):
    scored = []
    for cand in candidates:
        education = cand.get("education", "").lower()
        headline = cand.get("headline", "").lower()
        location = cand.get("location", "").lower()
        companies = cand.get("companies", [])

        edu_score = (
            9 if any(x in education for x in ["mit", "stanford", "berkeley"])
            else 7 if any(x in education for x in ["cmu", "uw", "uiuc"])
            else 5
        )
        trajectory_score = 8 if len(companies) >= 2 else 5
        company_score = 9 if any("google" in c.lower() or "openai" in c.lower() for c in companies) else 6
        skills_score = 8 if "ml" in headline or "llm" in headline else 6
        location_score = 10 if "mountain view" in location else 6
        tenure_score = 8  # Still placeholder

        total = (
            edu_score * 0.2 +
            trajectory_score * 0.2 +
            company_score * 0.15 +
            skills_score * 0.25 +
            location_score * 0.1 +
            tenure_score * 0.1
        )
        scored.append({
            **cand,
            "score": round(total, 2),
            "breakdown": {
                "education": edu_score,
                "trajectory": trajectory_score,
                "company": company_score,
                "skills": skills_score,
                "location": location_score,
                "tenure": tenure_score
            }
        })
    return scored
