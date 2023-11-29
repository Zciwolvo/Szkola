const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cookiePareser = require('cookie-parser');
const flash = require('connect-flash');
const session = require('express-session');
const routes = require('./routes/index');

const app = express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(cookiePareser());
app.use(session({
    secret: 'tajne haslo',
    resave: false,
    saveUninitialized: true,
    cookie: {}
}));

app.use(flash());

app.use('/', routes);

module.exports = app;