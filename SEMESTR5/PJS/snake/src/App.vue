<template>
  <div id="app">
    <div class="boards-container">
      <GameBoard />
      <ScoreBoard />
    </div>
  </div>
</template>

<script setup>
import GameBoard from './components/Board.vue';
import ScoreBoard from './components/ScoreBoard.vue';
</script>

<style>
#app {
  text-align: center;
  padding-top: 20px;
  display: flex;
}

.boards-container {
  display: flex;
  align-items: center;
  justify-content: center;
  justify-content: space-between;
}
</style>
