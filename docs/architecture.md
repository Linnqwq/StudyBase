# Architecture

## Overview
The system is a web-based AI study document organizer. It allows users to upload course materials, store them in the cloud, process document content, extract key information, and display organized results on the frontend.

## Main components

### Frontend
Responsible for the user interface.
Main responsibilities:
- user login and basic interaction
- course creation
- file upload interface
- document summary display
- course dashboard display

### Backend
Responsible for application logic and AI workflow.
Main responsibilities:
- receive file upload requests
- manage document metadata
- trigger document parsing
- call AI services for extraction and summarization
- return processed results to frontend

### Storage
Used for storing original uploaded files.
Examples:
- Supabase Storage
- AWS S3

### Database
Used for storing structured application data.
Examples of stored data:
- users
- courses
- documents
- extracted metadata
- summaries
- chunk records
- embeddings later if needed

### AI processing pipeline
Responsible for:
- parsing document text
- splitting text into chunks if needed
- extracting grading, deadlines, and policies
- generating document summaries
- supporting semantic retrieval in later versions

## Basic flow
1. User creates a course on the frontend
2. User uploads a document
3. File is stored in cloud storage
4. Backend records document metadata in database
5. Backend parses the file content
6. AI processing extracts useful information and generates summaries
7. Results are saved to database
8. Frontend displays organized course information to the user

## Suggested first-stack direction
- Frontend: Next.js
- Backend: FastAPI
- Database: PostgreSQL
- Storage: Supabase Storage or AWS S3

## Future extensions
- semantic search with embeddings
- document Q&A
- assignment reminder system
- study plan generation
- mobile companion app