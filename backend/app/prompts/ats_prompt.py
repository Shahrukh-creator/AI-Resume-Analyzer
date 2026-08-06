def get_ats_prompt(context: str):

    return f"""
You are an Applicant Tracking System.

Analyze this resume.

Provide:

1. ATS Score (0-100)

2. Strengths

3. Weaknesses

4. Missing Skills

5. Suggestions

Resume:

{context}
"""