# app/db.py
from pydantic import BaseModel
import psycopg2
from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    id: int
    title: str
    state: str

class BookCreate(BaseModel):
    title: str

class UpdateBookRequest(BaseModel):
    new_state: str

class BookRepository:
    def __init__(self):
        self.conn = psycopg2.connect(
            user="postgres",
            password="Fi3445supabase",
            host="db.ucekfljadhripdgtdziw.supabase.co",
            port=5432,
            database="postgres",
        )
        self.init_db()

    def init_db(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    state VARCHAR(255) NOT NULL
                );
            """)
        self.conn.commit()

    def create_book(self, title: str, state: str) -> int:
        with self.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO books(title, state) VALUES (%s, %s) RETURNING id",
                (title, state),
            )
            book_id = cursor.fetchone()[0]
        self.conn.commit()
        return book_id

    def get_all_books(self) -> List[Book]:
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT id, title, state FROM books")
            books = [Book(*row) for row in cursor.fetchall()]
        return books

    def get_book_by_id(self, book_id: int) -> Book:
        with self.conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, title, state FROM books WHERE id = %s", (book_id,)
            )
            row = cursor.fetchone()
            if row:
                return Book(*row)
            else:
                raise HTTPException(status_code=404, detail="Book not found")

    def update_book_state(self, book_id: int, state: str) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute(
                "UPDATE books SET state = %s WHERE id = %s",
                (state, book_id),
            )
        self.conn.commit()

    def delete_book(self, book_id: int) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        self.conn.commit()

def init_db():
    BookRepository().init_db()
