const express = require("express");
const { MongoClient } = require("mongodb");
const fs = require("fs");
const https = require("https");

const app = express();
const port = 5000;

const uri =
  "mongodb+srv://skapiec.4ju5ocq.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Skapiec";
const tlsCertificateKeyFile = "../certs/X509-cert-3621885173140152299.pem";

const client = new MongoClient(uri, {
  tls: true,
  tlsCertificateKeyFile: fs.readFileSync(tlsCertificateKeyFile),
  serverApi: { version: "1" },
});

app.use(express.json());

app.get("/todos", async (req, res) => {
  try {
    await client.connect();
    const db = client.db("todo");
    const collection = db.collection("todos");
    const todos = await collection.find({}).toArray();
    res.json(todos);
  } catch (error) {
    console.error("Error fetching todos:", error);
    res.status(500).json({ error: "Internal server error" });
  } finally {
    await client.close();
  }
});

// Define other CRUD endpoints as needed

https
  .createServer(
    {
      key: fs.readFileSync("path/to/key.pem"),
      cert: fs.readFileSync("path/to/cert.pem"),
    },
    app
  )
  .listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
