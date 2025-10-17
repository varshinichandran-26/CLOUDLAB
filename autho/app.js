require("dotenv").config();
const express = require("express");
const { auth } = require("express-openid-connect");

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json()); // optional, in case JSON is needed later

// ✅ Auth0 configuration
const config = {
  authRequired: false,
  auth0Logout: true,
  secret: process.env.AUTH0_SECRET,
  baseURL: process.env.AUTH0_BASE_URL || "http://localhost:3000",
  clientID: process.env.AUTH0_CLIENT_ID,
  issuerBaseURL: process.env.AUTH0_ISSUER_BASE_URL,
};

// ✅ Apply Auth0 auth middleware
app.use(auth(config));

// ✅ In-memory Todo list
let todos = [];

// ✅ Home route
app.get("/", (req, res) => {
  if (!req.oidc.isAuthenticated()) {
    return res.send(`
      <h2>Welcome to the Todo App</h2>
      <p>Please <a href="/login">Login</a> to continue.</p>
    `);
  }

  const userName = req.oidc.user?.name || "User";
  const todoList = todos.length
    ? todos.map((t) => `<li>${t}</li>`).join("")
    : "<li>No tasks yet</li>";

  res.send(`
    <h2>Hello, ${userName}</h2>
    <form method="POST" action="/add">
      <input name="task" placeholder="Enter task" required>
      <button type="submit">Add</button>
    </form>
    <ul>${todoList}</ul>
    <br>
    <a href="/logout">Logout</a>
  `);
});

// ✅ Add task route
app.post("/add", (req, res) => {
  if (req.oidc.isAuthenticated() && req.body.task?.trim()) {
    todos.push(req.body.task.trim());
  }
  res.redirect("/");
});

// ✅ Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () =>
  console.log(`✅ Server running at ${config.baseURL} on port ${PORT}`)
);


