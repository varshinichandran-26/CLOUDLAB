const express = require('express');
const app = express();

app.use(express.json()); // To parse JSON request body

// Sample data
let books = [
  { id: 1, title: 'Harry Potter' },
  { id: 2, title: 'Twilight' },
  { id: 3, title: 'Lorien Legacies' }
];

// Root route
app.get('/', (req, res) => {
  res.send('REST APIs with Express are working!');
});

// GET all books
app.get('/api/books', (req, res) => {
  res.send(books);
});

// GET book by ID
app.get('/api/books/:id', (req, res) => {
  const book = books.find(b => b.id === parseInt(req.params.id));
  if (!book) {
    return res.status(404).send('Book not found');
  }
  res.send(book);
});

// POST - Add new book
app.post('/api/books', (req, res) => {
  const book = {
    id: books.length + 1,
    title: req.body.title
  };
  books.push(book);
  res.send(book);
});

// PUT - Update book by ID
app.put('/api/books/:id', (req, res) => {
  const book = books.find(b => b.id === parseInt(req.params.id));
  if (!book) {
    return res.status(404).send('Book not found');
  }
  book.title = req.body.title;
  res.send(book);
});

// DELETE - Remove book by ID
app.delete('/api/books/:id', (req, res) => {
  const book = books.find(b => b.id === parseInt(req.params.id));
  if (!book) {
    return res.status(404).send('Book not found');
  }
  books = books.filter(b => b.id !== book.id);
  res.send(book);
});

// Start server
const port = 8080;

app.listen(port, () => console.log(`Server running on http://localhost:${port}`));

