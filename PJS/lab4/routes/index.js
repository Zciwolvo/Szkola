// inicjacja modułów
const express = require('express');
const router = express.Router();
// definicja kontrolerów w osobnych plikach
const PagesController = require('../controllers/PagesController');
const ApplicationsController = require('../controllers/ApplicationsController'
);
const zad2 = require('../controllers/zad2Controller');
const zad3 = require('../controllers/zad3Controller');
const zad4 = require('../controllers/zad4Controller');
// połączenie tras z poszczególnymi kontrolerami
router.get('/', PagesController.home);
router.get('/phrase', PagesController.home)
router.post('/applications', ApplicationsController.store);

router.get('/nowy', (req, res) => {
      return res.redirect(301, '/serwer1');
  });

  router.get('/witaj', zad2.welcome);

  router.get('/zad3', zad3.zad3);

router.get('/nowa', (req, res) => {
    res.write('To jest nowa strona!');
    res.end();
  });
  
  router.get('/stara', (req, res) => {
    res.write('To jest stara strona!');
    res.end();
  });


module.exports = router;
