from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models import Document, Course
from services.storage import upload_file, ALLOWED_MIME_TYPES
import uuid

router = APIRouter(prefix="/courses/{course_id}/documents", tags=["documents"])

@router.post("/")
async def upload_document(
    course_id: uuid.UUID,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    # 检查课程存在
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="课程不存在")

    # 检查文件类型
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400, detail="只支持 PDF、PPTX、DOCX 格式")

    # 读取文件内容
    file_bytes = await file.read()

    # 上传到 Supabase Storage
    storage_path, storage_url = upload_file(file_bytes, file.content_type, str(course_id))

    # 写入数据库
    document = Document(
        course_id=course_id,
        original_filename=file.filename,
        storage_path=storage_path,
        storage_url=storage_url,
        file_size=len(file_bytes),
        mime_type=file.content_type,
    )
    db.add(document)
    await db.flush()

    return {
        "id": str(document.id),
        "filename": document.original_filename,
        "size": document.file_size,
        "url": document.storage_url,
    }