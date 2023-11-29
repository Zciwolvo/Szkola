var express = require('express');
var app = express();
var path = require('path');


app.get('/nowa', function (req, res) {
    res.sendFile(path.join(__dirname, 'nowa/index.html'));
});

app.get('/stara', function (req, res) {
    res.sendFile(path.join(__dirname, 'stara/index.html'));
});

app.listen(80);
console.log('Listening on port 80');