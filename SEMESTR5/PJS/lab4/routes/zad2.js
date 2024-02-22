const express = require('express');
const router = express.Router();

const zad2 = require('../controllers/zad2Controller');

router.get('/witaj', zad2.welcome);

module.exports = router;