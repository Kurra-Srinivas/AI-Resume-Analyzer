from llm_helper import llm

def generate_roadmap(resume_text, target_role):
    prompt = f"""
You are a career coach. Given the following resume and a target role: '{target_role}', do the following:
1. Analyze candidate fit
2. Identify skill/tool gaps
3. Generate a roadmap with learning steps and resources
4. Rewrite 2-3 resume bullet points to better match the target
5. Generate a 3-line LinkedIn post to announce career intent

Resume:
\"\"\"
{resume_text}
\"\"\"
"""
    response = llm.invoke(prompt)
    return response.content


def evaluate_resume(resume_text, tone="General", language="English"):
    prompt = f"""
You are a professional career counselor and resume expert.

Your task is to evaluate the following resume text in terms of content quality, structure, formatting, keywords, and overall effectiveness.

Tone: {tone}
Output Language: {language}

Resume Text:
\"\"\"
{resume_text}
\"\"\"

Evaluation Guidelines:
- Start with 1–2 line summary of the resume’s strengths
- Highlight specific weaknesses or areas for improvement
- Recommend 2–3 actionable suggestions
- End with a final rating out of 10

Respond in detailed but readable language.
"""
    response = llm.invoke(prompt)
    return response.content.strip()
