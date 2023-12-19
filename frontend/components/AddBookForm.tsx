// components/AddBookForm.tsx
import React, { useState } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';

interface AddBookFormProps {
  onAddBook: (title: string) => void;
}

const AddBookForm: React.FC<AddBookFormProps> = ({ onAddBook }) => {
  const [title, setTitle] = useState('');

  const handleAddBook = () => {
    if (title.trim() !== '') {
      onAddBook(title);
      setTitle('');
    }
  };

  return (
    <div className=" flex justify-center items-center gap-4">
      <Input
        type="text"
        placeholder="Enter book title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <Button onClick={handleAddBook}>Add Book</Button>
    </div>
  );
};

export default AddBookForm;