// types/types.ts
export interface Book {
    id: number;
    title: string;
    state: 'to-read' | 'in-progress' | 'completed';  
  }
  