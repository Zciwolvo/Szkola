const express = require('express');
const fs = require('fs');
const cors = require('cors');
const path = require('path');
const app = express();

app.use(cors());
app.use(express.json());

const dataFilePath = path.join(__dirname, 'data.json');


app.post('/addData', (req, res) => {
    const { score } = req.body; 
  
    if (!score || isNaN(score)) {
      return res.status(400).send('Invalid score');
    }
  
    const newEntry = {
      datetime: new Date().toISOString(),
      score: parseInt(score),
    };

  fs.readFile(dataFilePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Error reading file');
    }

    let entries = [];
    if (data) {
      entries = JSON.parse(data);
    }

    entries.push(newEntry);

    fs.writeFile(dataFilePath, JSON.stringify(entries, null, 2), (err) => {
      if (err) {
        return res.status(500).send('Error writing file');
      }
    });
  });
});

app.get('/getData', (req, res) => {
    fs.readFile(dataFilePath, 'utf8', (err, data) => {
      if (err) {
        return res.status(500).send('Error reading file');
      }
      const jsonData = JSON.parse(data);
      res.json(jsonData);
    });
  });
  

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
