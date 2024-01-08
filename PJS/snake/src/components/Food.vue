<template>
    <div
      :style="getFoodCellStyle()"
    ></div>
  </template>
  
  <script>
  export default {
    props: ['food'],
  
    methods: {
      getFoodCellStyle() {
        return {
          width: '20px',
          height: '20px',
          border: '1px solid #ccc',
          backgroundColor: '#ff0000',
          position: 'relative',
          top: `${this.food.row * 20}px`,
          left: `${this.food.col * 20}px`,
        };
      },
    },
  };
  </script>
  
  <style scoped>
  div {
    width: 20px;
    height: 20px;
    border: 1px solid #ccc;
    background-color: #FF0000;
    position: absolute;
  }
  </style>
  
  