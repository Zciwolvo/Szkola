// inicjacja modułów
const express = require('express');
const router = express.Router();
// definicja kontrolerów w osobnych plikach
const PagesController = require('../controllers/PagesController');
const ApplicationsController = require('../controllers/ApplicationsController'
);
// połączenie tras z poszczególnymi kontrolerami
router.get('/', PagesController.home);
router.get('/phrase', PagesController.home)
router.post('/applications', ApplicationsController.store);

//Zadanie 1
router.get('/nowy', (req, res) => {
      return res.redirect(301, '/serwer1');
  });

//Zadanie 2
const zad2 = require('../controllers/zad2Controller');
router.get('/witaj', zad2.welcome);

//Zadanie 3
const zad3 = require('../controllers/zad3Controller');
router.get('/zad3', zad3.zad3);

//Zadanie 4
router.get('/nowa', (req, res) => {
    res.write('To jest nowa strona!');
    res.end();
  });
  
  router.get('/stara', (req, res) => {
    res.write('To jest stara strona!');
    res.end();
  });

//Zadanie 7

const zad7 = require('../controllers/zad7Controller');

router.get('/z7nowa', zad7.Z7nowa);
router.get('/z7stara', zad7.Z7stara);


module.exports = router;
  