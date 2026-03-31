from fastapi import FastAPI
from routers import courses, documents

app = FastAPI(title="StudyBase API")

app.include_router(courses.router)
app.include_router(documents.router)

@app.get("/")
def root():
    return {"message": "StudyBase API is running"}