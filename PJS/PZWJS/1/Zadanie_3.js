/*Napisać program, który generuje event w
przypadku żądania www do serwera*/

const { EventEmitter } = require('events');
var events = require('events');
var eventEmitter = new events.EventEmitter();
var myEventHandler = function(){
    console.log('I hear a scream');
}
eventEmitter.on('scream', myEventHandler);

var http = require('http');
var port = 8080;
var server = http.createServer(function(request, response)
{
    response.end('Pierwszy serwer HTTP w Node JS');
    request.addListener('end', function(){
        eventEmitter.emit('scream');
    });
});
