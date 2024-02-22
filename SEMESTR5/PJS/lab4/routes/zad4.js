const express = require('express');
const router = express.Router();

router.get('/nowa', (req, res) => {
    res.write('To jest nowa strona!');
    res.end();
  });
  
  router.get('/stara', (req, res) => {
    res.write('To jest stara strona!');
    res.end();
  });

module.exports = router;