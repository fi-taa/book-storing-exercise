from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse
import json
from app.db import BookRepository, init_db, Book, BookCreate, UpdateBookRequest


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",  # Add the URL of your frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database initialization
init_db()

    
@app.post("/books/", response_model=dict)
async def create_book(book: BookCreate):
    book_id = BookRepository().create_book(book.title, "to-read")
    return {"id": book_id}


@app.get("/books/", response_model=List[Book])
async def read_books():
    return BookRepository().get_all_books()


@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    return BookRepository().get_book_by_id(book_id)


@app.put("/books/{book_id}", response_model=dict)
async def update_book(book_id: int, request: UpdateBookRequest):
    try:
        # Validate that the state is one of the allowed values
        valid_states = ['to-read', 'in-progress', 'completed']
        if request.new_state not in valid_states:
            raise HTTPException(status_code=422, detail="Invalid state")

        # Update the book state
        BookRepository().update_book_state(book_id, request.new_state)
        return {"message": "Book updated successfully"}
    except HTTPException as e:
        return JSONResponse(
            content=json.dumps({"error": e.detail}), status_code=e.status_code
            )


@app.delete("/books/{book_id}", response_model=dict)
async def delete_book(book_id: int):
    BookRepository().delete_book(book_id)
    return {"message": "Book deleted successfully"}
