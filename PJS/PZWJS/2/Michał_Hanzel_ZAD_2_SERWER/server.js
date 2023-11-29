const app = require('./app');

var port = process.env.PORT || 8080;

const server = app.listen(port, () => {
    console.log(`Listening on ${server.address().port}`);
});