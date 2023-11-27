var express = require('express');
var pug = require('pug');

var app = express();

app.set('views', './pug');
app.set('view engine', 'pug');

app.engine('pug', pug.__express);

app.listen(80);

app.locals = { uname: 'Tadeusz', usurname: "Kowalski" };

app.get('/pug', function (req, res) {
    res.render('user_jade');
});