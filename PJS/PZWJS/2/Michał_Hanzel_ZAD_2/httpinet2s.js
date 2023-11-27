var http = require('http');
var url = require('url');
var fs = require('fs');

var tab = [];
var element = function (znak, x, y) {
    return { znak: znak, x: x, y: y };
}
const options = {
    key: fs.readFileSync('key.pem'),
    cert: fs.readFileSync('cert.pem')
};

http.createServer(options, function (req, res) {
    var q = url.parse(req.url, true);

    var fileName = "." + q.pathname;

    if (q.pathname == "/client") {
        var jsData = '';

        req.on('data', function (chunk) {
            jsData += chunk;
        });
        req.on('end', function () {
            var ob = JSON.parse(jsData);
            tab.push(element(ob.znak, ob.x, ob.y));
            for (var i = 0; i < tab.length; i++) {
                console.log(i + ": znak: " + tab[i].znak + " | x: " + tab[i].x + " | y: " + tab[i].y);
            }
            var ob = tab;

            res.writeHead(200);
            res.end(JSON.stringify(ob));
        });

    }
    if (q.pathname != "/client")
        fs.readFile(fileName, function (err, data) {
            if (err) {
                res.writeHead(404, { 'Content-Type': 'text/html' });
                return res.end("404 Not Found");
            }
            res.writeHead(200, { 'Content-Type': 'text/html' });

            for (var i = 0; i < tab.length; i++) {
                res.write("<br>" + i + ": znak: " + tab[i].znak + " | x: " + tab[i].x + " | y: " + tab[i].y);
            }
            return res.end();
        });
}).listen(8080); 