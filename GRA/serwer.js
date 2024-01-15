const express = require('express');
const cors = require('cors')
const app = express();
const port = 3000;


app.use(cors())

let wordList = ['jablko', 'banan', 'pomarańcza', 'cytryna', 'kiwi','mango','wiśnia','czereśnia'];
let currentWord = '';
let hiddenWord = [];
let attemptsLeft = 6;
let correctGuesses = 0;
let playerScore = 0;

function startNewGame() {
  currentWord = getRandomWord();
  hiddenWord = Array(currentWord.length).fill('_');
  attemptsLeft = 6;
  correctGuesses = 0;
}

function getRandomWord() {
  return wordList[Math.floor(Math.random() * wordList.length)];
}

app.use(express.json());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/game-state', (req, res) => {
  res.json({
    hiddenWord,
    attemptsLeft,
    playerScore
  });
});

app.post('/guess/:letter', (req, res) => {
  const guessedLetter = req.params.letter.toLowerCase();

  if (!currentWord.includes(guessedLetter)) {
    attemptsLeft--;
  } else {
    for (let i = 0; i < currentWord.length; i++) {
      if (currentWord[i] === guessedLetter && hiddenWord[i] === '_') {
        hiddenWord[i] = guessedLetter;
        correctGuesses++;
      }
    }
  }

  if (attemptsLeft === 0 || correctGuesses === currentWord.length) {
    if (correctGuesses === currentWord.length) {
      playerScore++;
    }
    startNewGame();
  }

  res.json({
    hiddenWord,
    attemptsLeft,
    playerScore
  });
});

startNewGame();

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
