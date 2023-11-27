var net = require('net');

var server = net.createServer(function (client) {
    console.log('Connection estabilished.');

    client.on('data', function (data) {
        console.log('Data received from client: ' + data.toString());
    });

    client.on('end', function () {
        console.log('Client disconnected.');
    });

    client.write('Welcome to our system.');
});

server.listen(8107, function () {
    console.log('Waiting for connection...');
});
