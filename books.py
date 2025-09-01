from fastapi import FastAPI
from pydantic import BaseModel

from typing import Optional


app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int   
    category: str


books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "category": "Fiction"}, 
    {"title": "1984", "author": "George Orwell", "year": 1949, "category": "Dystopian"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "category": "Fiction"},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "year": 1988, "category": "Science"},
    {"title": "The Art of War", "author": "Sun Tzu", "year": -500, "category": "Philosophy"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "category": "Fiction"},
    
    ]   


@app.get("/books/")
async def read_books():
    return books

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return books[book_id]

@app.post("/books/")
async def create_book(book: Book):
    books.append(book.dict())
    return {
        "message": "Item created successfully!",
        "item": book
    }
 

# Search endpoint
@app.get("/books/search/")
async def search_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    category: Optional[str] = None
):
    results = books
    if title:
        results = [book for book in results if title.lower() in book["title"].lower()]
    if author:
        results = [book for book in results if author.lower() in book["author"].lower()]
    if year:
        results = [book for book in results if book["year"] == year]
    if category:
        results = [book for book in results if category.lower() in book["category"].lower()]
    return results


