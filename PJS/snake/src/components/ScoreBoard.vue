<template>
    <div>
      <h1 style="color: #fff;">Scoreboard</h1>
  
      <table>
        <thead>
          <tr>
            <th>Date/Time</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, index) in entries" :key="index" :style="getRowStyle(index)">
            <td>{{ entry.datetime }}</td>
            <td>{{ entry.score }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        entries: [],
      };
    },
    created() {
      this.getData();
    },
    methods: {
      async getData() {
        try {
          const response = await axios.get('http://localhost:3000/getData');
          this.entries = response.data;
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
      getRowStyle(index) {
        return {
          backgroundColor: index % 2 === 0 ? '#333' : '#444',
          color: '#fff',
          padding: '8px',
        };
      },
    },
  };
  </script>
  
  <style scoped>
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  th {
    background-color: #181818;
    font-weight: bold;
    text-align: left;
    padding: 8px;
  }
  
  td {
    padding: 8px;
  }
  
  tr:hover {
    background-color: #555;
  }
  </style>
  