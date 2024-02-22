
const express = require('express');
const router = express.Router();


router.get('/zad3', zad3.zad3);

const zad3 = require('../controllers/zad3Controller');

module.exports = router;