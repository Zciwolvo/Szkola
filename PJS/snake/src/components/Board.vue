<template>
    <div class="board">
        <Snake :snake="snake" :score="score" />
      <Food :food="food" />
  
      <div v-if="!gameRunning">
        <button @click="startGame">Start Game</button>
      </div>
    </div>
  </template>
  
  <script>
  import Snake from './Snake.vue';
  import Food from './Food.vue';
  import axios from 'axios';
  
  export default {
    components: {
      Snake,
      Food,
    },
    data() {
      return {
        width: 20, // Board width (number of cells)
        height: 20, // Board height (number of cells)
        snake: [{ row: 10, col: 10 }], // Snake initial position
        food: {}, // Food position
        direction: 'right', // Initial direction
        gameRunning: false, // Game state
        intervalId: null, // Timer ID for snake movement
        score: 0,
      };
    },
    methods: {
      startGame() {
        this.gameRunning = true;
        this.generateFood(); // Generate initial food
        this.intervalId = setInterval(this.moveSnake, 200); // Snake movement interval
        this.score = 0;
      },
      moveSnake() {
        // Logic to move the snake
        const head = { ...this.snake[0] };
        switch (this.direction) {
          case 'up':
            head.row--;
            break;
          case 'down':
            head.row++;
            break;
          case 'left':
            head.col--;
            break;
          case 'right':
            head.col++;
            break;
        }
  
        this.snake.unshift(head); // Add new head
        if (this.isFoodEaten()) {
            this.score++
          this.generateFood(); // Generate new food
        } else {
          this.snake.pop(); // Remove tail
        }
  
        if (this.isCollision()) {
          this.addData();
          this.endGame();
        }
      },
      isFoodEaten() {
        return this.snake[0].row === this.food.row && this.snake[0].col === this.food.col;
      },
      generateFood() {
        const row = Math.floor(Math.random() * this.height);
        const col = Math.floor(Math.random() * this.width);
  
        this.food = { row, col };
      },
      isCollision() {
        const head = this.snake[0];
        
        // Check collision with walls
        if (head.row < 0 || head.col < 0 || head.row >= this.height || head.col >= this.width) {
          return true;
        }
  
        // Check collision with itself
        for (let i = 1; i < this.snake.length; i++) {
          if (head.row === this.snake[i].row && head.col === this.snake[i].col) {
            return true;
          }
        }
  
        return false;
      },
      endGame() {
        clearInterval(this.intervalId); // Stop the timer
        this.gameRunning = false;
        this.snake = [{ row: 10, col: 10 }]; // Reset snake position
      },

      async addData() {
        try {
            if (!this.score || isNaN(this.score)) {
            alert('Score lower than 1 will not be added to scoreboard!');
            return;
            }

            const response = await axios.post('http://localhost:3000/addData', {
            score: this.score,
            });

            if (response.status === 200) {
            alert('Data added successfully');
            } else {
            alert('Failed to add data');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while adding data');
        }
        },

    },
    created() {
      document.addEventListener('keydown', (event) => {
        switch (event.key) {
          case 'ArrowUp':
            this.direction = 'up';
            break;
          case 'ArrowDown':
            this.direction = 'down';
            break;
          case 'ArrowLeft':
            this.direction = 'left';
            break;
          case 'ArrowRight':
            this.direction = 'right';
            break;
        }
      });
    },
  };
  </script>
  
  <style scoped>
  .board {
    display: grid;
    grid-template-columns: repeat(20, 20px);
    grid-template-rows: repeat(20, 20px);
    width: 400px; /* Adjust board size */
    height: 400px; /* Adjust board size */
    border: 1px solid #000; /* Board border */
  }
  
  .board > div {
    background-color: #fff; /* Default cell color */
  }
  </style>
  