// components/BookItem.tsx
import React from 'react';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'; 
// import { Button } from '@/components/ui/button';
import { Book } from '../types/types';

interface BookItemProps {
  book: Book;
  onMoveBook: (bookId: number, newState: 'to-read' | 'in-progress' | 'completed') => void;
  onDeleteBook: (bookId: number) => void;
}

const BookItem: React.FC<BookItemProps> = ({ book, onMoveBook, onDeleteBook }) => {
  return (
    <div className="flex justify-between md:w-48 w-32 items-center text-xs  md:text-base ">
      <p className="">{book.title}</p>
      <div className='flex justify-center items-center gap-2'>
      <DropdownMenu>
        <DropdownMenuTrigger>
          <img src="/move.png" alt="" className='w-4 hover:w-5 rotate-90' />
        </DropdownMenuTrigger>
        <DropdownMenuContent>
          <DropdownMenuItem onSelect={() => onMoveBook(book.id, 'to-read')}>To Read</DropdownMenuItem>
          <DropdownMenuItem onSelect={() => onMoveBook(book.id, 'in-progress')}>In Progress</DropdownMenuItem>
          <DropdownMenuItem onSelect={() => onMoveBook(book.id, 'completed')}>Completed</DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>

      {/* Delete button */}
      <button onClick={() => onDeleteBook(book.id)}>
      <img src="/delete.png" alt="" className='w-4 hover:w-5' />
      </button>

      </div>

    </div>
  );
};

export default BookItem;
