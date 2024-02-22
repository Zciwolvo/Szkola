<template>
    <div>
      <div v-for="(cell, index) in snake" :key="index" :style="getSnakeCellStyle(cell)"></div>
      <p>Score: {{ score }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: ['snake', 'score'],
  
    methods: {
      getSnakeCellStyle(cell) {
        return {
          width: '20px',
          height: '20px',
          border: '1px solid #ccc',
          backgroundColor: '#333',
          position: 'absolute',
          top: `${cell.row * 20}px`,
          left: `${cell.col * 20}px`,
        };
      },
    },
  };
  </script>
  
  <style scoped>
  div {
    position: relative;
  }
  
  div > div {
    background-color: #333;
    border: 1px solid #ccc;
    width: 20px;
    height: 20px;
    position: absolute;
  }
  
  div > div:first-child {
    background-color: #181818;
    border: none;
  }
  
  div > div:last-child {
    background-color: #FFC107;
  }
  </style>
  
  