const https = require('https');
const url = require('url');
const fs = require('fs');
const { eachSeries } = require('async');

const options = {
    key: fs.readFileSync('key.pem'),
    cert: fs.readFileSync('cert.pem')
};

https.createServer(options, function (req, res) {
    var q = url.parse(req.url, true);

    var fileName = "." + q.pathname;

    fs.readFile(fileName, function (err, data) {
        if (err) {
            res.writeHead(404, { 'Content-Type': 'text/html' });
            return res.end("404 Not Found");
        }
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(data);
        return res.end();
    });

}).listen(8080);