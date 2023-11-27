var net = require('net');
var fs = require('fs');

var tosend;

tosend = fs.readFileSync('tosend.txt').toString();

var client = net.connect({ port: 8107, host: 'localhost' }, function () {
    console.log('Estabilishing connection to client.');
    client.write(tosend);
});

client.on('data', function (data) {
    console.log(data.toString());
    client.end();
});

client.on('end', function (data) {
    console.log('Client has been disconnected.');
});
