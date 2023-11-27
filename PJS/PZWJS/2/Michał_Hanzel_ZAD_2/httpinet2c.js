var http = require('http');

var options = {
    hostname: 'localhost',
    path: '/client',
    port: '8080',
    method: 'POST'
};
function handleResponse(response) {
    var str = '';
    response.on('data', function (chunk) {
        str += chunk;

    });

    response.on('end', function () {
        jsData = JSON.parse(str);
        console.log(jsData);
    });
};

for (var i = 0; i < 3; i++) {
    console.log("Iteration: " + i);
    var req = http.request(options, handleResponse);
    req.write('{"znak":"#", "x":' + i + ', "y":' + i % 2 + '}');
    req.end();
}