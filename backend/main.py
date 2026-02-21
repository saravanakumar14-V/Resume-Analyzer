from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pdfplumber
import docx
import io

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (OK for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# SIMPLE SKILL LIST
# -----------------------------
skills = [
    "python",
    "java",
    "sql",
    "machine learning",
    "fastapi",
    "django",
    "react",
    "docker"
]

# -----------------------------
# RESUME ANALYSIS FUNCTION
# -----------------------------
def analyze_resume(text: str):
    text_lower = text.lower()
    found_skills = []

    for skill in skills:
        if skill in text_lower:
            found_skills.append(skill)

    score = min(len(found_skills) * 10, 100)

    return {
        "score": score,
        "skills_found": found_skills,
        "total_skills": len(found_skills)
    }

# -----------------------------
# JOB MATCHING FUNCTION
# -----------------------------
def match_job(resume_text: str, job_text: str):
    resume_text = resume_text.lower()
    job_text = job_text.lower()

    resume_skills = [s for s in skills if s in resume_text]
    job_skills = [s for s in skills if s in job_text]

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    match_percent = int((len(matched) / max(len(job_skills), 1)) * 100)

    return {
        "match_percentage": match_percent,
        "matched_skills": matched,
        "missing_skills": missing
    }

# -----------------------------
# SUGGESTION FUNCTION
# -----------------------------
def resume_suggestions(match_result: dict):
    suggestions = []

    if match_result["match_percentage"] < 50:
        suggestions.append(
            "Your resume has low relevance. Add more job-specific skills."
        )

    if match_result["missing_skills"]:
        suggestions.append(
            "Consider adding these skills: " +
            ", ".join(match_result["missing_skills"])
        )

    if not suggestions:
        suggestions.append("Your resume matches the job well.")

    return suggestions

# -----------------------------
# REQUEST MODEL
# -----------------------------
class JobMatchRequest(BaseModel):
    resume_text: str
    job_description: str

# -----------------------------
# ROUTES
# -----------------------------
@app.get("/")
def root():
    return {"status": "Backend is working"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    text = ""

    if file.filename.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(await file.read())) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif file.filename.endswith(".docx"):
        doc = docx.Document(io.BytesIO(await file.read()))
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        return {"error": "Unsupported file format"}

    analysis = analyze_resume(text)

    return {
        "filename": file.filename,
        "analysis": analysis,
        "preview": text[:500]
    }

@app.post("/match-job")
def match_job_api(data: JobMatchRequest):
    return match_job(data.resume_text, data.job_description)

@app.post("/resume-suggestions")
def suggestions_api(data: JobMatchRequest):
    match_result = match_job(data.resume_text, data.job_description)
    suggestions = resume_suggestions(match_result)

    return {
        "match": match_result,
        "suggestions": suggestions
    }