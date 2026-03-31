import uuid
from supabase import create_client
from config import settings

ALLOWED_MIME_TYPES = {
    "application/pdf": ".pdf",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": ".pptx",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
}

def get_supabase():
    return create_client(settings.supabase_url, settings.supabase_secret_key)

def upload_file(file_bytes: bytes, mime_type: str, course_id: str) -> tuple[str, str]:
    client = get_supabase()
    
    ext = ALLOWED_MIME_TYPES[mime_type]
    storage_path = f"courses/{course_id}/{uuid.uuid4()}{ext}"
    
    client.storage.from_(settings.storage_bucket).upload(
        path=storage_path,
        file=file_bytes,
        file_options={"content-type": mime_type},
    )
    
    url = client.storage.from_(settings.storage_bucket).get_public_url(storage_path)
    
    return storage_path, url