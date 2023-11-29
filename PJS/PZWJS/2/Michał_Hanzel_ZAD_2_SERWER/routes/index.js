const express = require('express');
const router = express.Router();

//controller
const PagesController = require('../controllers/PagesController');

//strony
router.get('/', PagesController.home);
router.get('/home', PagesController.home);
router.get('/second-page', PagesController.secondPage);
router.get('/third-page', PagesController.thirdPage);
router.get('/fourth-page', PagesController.fourthPage);

//export
module.exports = router;