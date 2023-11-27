var fs = require('fs');
var replaceStream = require('replacestream');
var readerStream = fs.createReadStream('plik.txt');
var writeStream = fs.createWriteStream('plik_zapisz.txt');

readerStream.setEncoding('UTF8');
readerStream.pipe(process.stdout);

readerStream.pipe(replaceStream(/[^a-z /s]/gi, '')).pipe(process.stdout);

var p_cezar = 3;

function cezar (znak){
    znak = znak.toLowerCase();
    var temp = znak.charCodeAt(0) + p_cezar;
    if(temp>122){
        temp = 97 + (temp-122);
    }
    return String.fromCharCode(temp);
}

readerStream.pipe(replaceStream(/([a-z])/gi, cezar)).pipe(process.stdout);

readerStream.pipe(replaceStream(/[^a-z /s]/gi, ''))
            .pipe(replaceStream(/([a-z])/gi, cezar))
            .pipe(writeStream);