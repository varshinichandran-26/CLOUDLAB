const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { MongoClient, ObjectId } = require('mongodb');

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(express.static('public')); // serves index.html

// === MongoDB Atlas connection ===
const uri = "mongodb+srv://cvarshini_db_user:varshini@cluster0.zd4yk5q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const client = new MongoClient(uri);

let collection;

// Connect to MongoDB
async function connectDB() {
  try {
    await client.connect();
    const db = client.db("BookDB");
    collection = db.collection("books");
    console.log("✅ Connected to MongoDB Atlas");
  } catch (err) {
    console.error("❌ DB Connection Error:", err);
  }
}
connectDB();

// ➕ Create
app.post('/add', async (req, res) => {
  const data = req.body;
  const result = await collection.insertOne(data);
  res.json(result);
});

// 📖 Read
app.get('/list', async (req, res) => {
  const result = await collection.find().toArray();
  res.json(result);
});

// ✏ Update
app.put('/update/:id', async (req, res) => {
  const id = req.params.id;
  const updated = req.body;
  const result = await collection.updateOne(
    { _id: new ObjectId(id) },
    { $set: updated }
  );
  res.json(result);
});

// ❌ Delete
app.delete('/delete/:id', async (req, res) => {
  const id = req.params.id;
  const result = await collection.deleteOne({ _id: new ObjectId(id) });
  res.json(result);
});

// 🚀 Start server
app.listen(3000, () => console.log("Server running → http://localhost:3000"));
