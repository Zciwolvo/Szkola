

// import modułów wykorzystywanych do utworzenia serwera
const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const flash = require('connect-flash');
const session = require('express-session');
const routes = require('./routes/index');
// obiekt serwer zwracany jako element modułu
const app = express();
// definiowanie silnika dla generowania widoków (w tym przypadku pug)
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');
// definicja statycznych zasobów: strony, grafika czy style
app.use(express.static(path.join(__dirname, 'public')));
// rozszerzenie funkcjonalności o nowe moduły
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
// wsparcie dla ciasteczek I sesji
app.use(cookieParser());
app.use(session({
 secret: 'tajne haslo',
 resave: false,
 saveUninitialized: true,
 cookie: {}
}));
// możliwość przesyłania informacji flash
app.use(flash());
// zarządzanie trasami - dwustopniowo
app.use('/', routes);
// przesłanie konfiguracji
module.exports = app;