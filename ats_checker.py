def check_ats_compliance(resume_text, target_role):
    prompt = f"""
    You are an ATS (Applicant Tracking System) simulation engine.

    Evaluate the following resume for compatibility with typical ATS software and a job role of "{target_role}".

    Provide:
    1. Formatting issues that could hurt ATS parsing
    2. Missing keywords or sections expected for the role
    3. A score out of 10 for ATS compatibility
    4. 2-3 recommendations to improve ATS success

    Resume:
    \"\"\"{resume_text}\"\"\"
    """
    from llm_helper import llm
    response = llm.invoke(prompt)
    return response.content.strip()
