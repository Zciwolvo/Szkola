var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);
var guid = require('uuid');

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

var numClients = 0;
var clients = [];

io.on('connection', function (socket) {

    if (numClients < 6) {
        numClients++;

        var newId = guid.v4();
        clients.push(newId);

        io.emit('stats', { numClients: numClients });

        console.log('Connected clients:', numClients);

        socket.on('disconnect', function () {
            numClients--;

            for (var i = 0; i < clients.length; i++) {

                if (clients[i] === newId) {

                    clients.splice(i, 1);
                }

            }

            io.emit('stats', { numClients: numClients });

            console.log('Connected clients:', numClients);
        });
    }
});

server.listen(8080);