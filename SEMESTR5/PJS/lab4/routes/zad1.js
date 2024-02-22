const express = require('express');
const router = express.Router();

router.get('/nowy', (req, res) => {
    return res.redirect(301, '/serwer1');
});

module.exports = router;