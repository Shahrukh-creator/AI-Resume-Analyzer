def get_summary_prompt(context: str):

    return f"""
You are an expert HR recruiter.

Read the resume below and write a professional summary.

Include:

- Candidate profession
- Years of experience
- Technical skills
- Education
- Key achievements

Resume:

{context}
"""