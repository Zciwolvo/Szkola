
var express = require('express');
var app = express();
var path = require('path');

app.get('/route', function (req, res) {
    res.sendFile(path.join(__dirname, 'route/index.html'));
});

app.all('/secret', function (req, res, next) {
    console.log('Accessing the secret section ...')
    res.sendFile(path.join(__dirname, 'route/index2.html'));
});

app.listen(80);
console.log('Listening on port 80');