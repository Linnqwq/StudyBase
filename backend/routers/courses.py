from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models import Course

router = APIRouter(prefix="/courses", tags=["courses"])

@router.post("/")
async def create_course(name: str, description: str = None, db: AsyncSession = Depends(get_db)):
    course = Course(name=name, description=description)
    db.add(course)
    await db.flush()
    return {"id": str(course.id), "name": course.name, "description": course.description}

@router.get("/")
async def list_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course))
    courses = result.scalars().all()
    return [{"id": str(c.id), "name": c.name, "description": c.description} for c in courses]