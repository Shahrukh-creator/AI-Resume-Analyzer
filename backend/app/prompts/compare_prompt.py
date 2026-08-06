def get_compare_prompt(
    context: str,
    job_description: str
):

    return f"""
You are an experienced recruiter.

Compare this resume with the Job Description.

Resume:

{context}

Job Description:

{job_description}

Provide:

1. Match Percentage

2. Matching Skills

3. Missing Skills

4. Candidate Strengths

5. Weaknesses

6. Suggestions
"""