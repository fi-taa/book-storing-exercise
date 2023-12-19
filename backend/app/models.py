# app/models.py
from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    state: str


class BookCreate(BaseModel):
    title: str


class UpdateBookRequest(BaseModel):
    new_state: str
