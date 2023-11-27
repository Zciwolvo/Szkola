var file = require('file');

//Asynchoniczne
file.redFile('plik.txt', function (err,data){
    if (err)
    {
        return console.error(err);
    }
    console.log(data.toString());
});

//Synchronicznie
var file2 = file.redFileSync('plik.txt');
console.log(data.toString());