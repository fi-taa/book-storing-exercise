// components/BookList.tsx
import React from 'react';
import BookItem from './BookItem';
import { Book } from '../types/types';

interface BookListProps {
  books: Book[];
  onMoveBook: (bookId: number, newState: 'to-read' | 'in-progress' | 'completed') => void;
  onDeleteBook: (bookId: number) => void;
}

const BookList: React.FC<BookListProps> = ({ books, onMoveBook, onDeleteBook }) => {
  return (
    <div className="space-y-4">
      {books.map((book) => (
        <BookItem key={book.id} book={book} onMoveBook={onMoveBook} onDeleteBook={onDeleteBook} />
      ))}
    </div>
  );
};

export default BookList;
