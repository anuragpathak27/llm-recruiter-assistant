import json

def store_data(candidates, messages, job_id="default"):
    data = {
        "job_id": job_id,
        "candidates": candidates,
        "messages": messages
    }
    with open(f"results_{job_id}.json", "w") as f:
        json.dump(data, f, indent=2)

