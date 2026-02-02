import pandas as pd
import random

def generate_job_data():
    jobs = [
        "Data Analyst",
        "Data Scientist",
        "ML Engineer",
        "AI Engineer",
        "Backend Developer",
        "Cloud Engineer",
        "HR Analyst"
    ]

    data = {
        "Job Role": random.choices(jobs, k=100)
    }

    df = pd.DataFrame(data)
    return df
