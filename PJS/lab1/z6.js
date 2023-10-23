let alphabetASCII = '';
for (let i = 65; i <= 90; i++) {
    alphabetASCII += String.fromCharCode(i) + ' ';
}

let alphabetUTF8 = '';
for (let i = 65; i <= 90; i++) {
    alphabetUTF8 += String.fromCodePoint(i) + ' ';
}

document.getElementById('alphabetASCII').textContent = 'Alfabet w ASCII:\n' + alphabetASCII;
document.getElementById('alphabetUTF8').textContent = 'Alfabet w UTF-8:\n' + alphabetUTF8;

const textArt = document.getElementById('textArt');

const rows = 11;
const cols = 80;

let art = '';
for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
        if (i < 2) {
            art += '.'
        }
        else if (i == 2 & j > 28 & j < 50){
            art += 'x'
        }
        else if (i == 3 & j > 27 & j < 51){
            art += 'x'
        }
        else if (i == 4 & j > 26 & j < 52){
            art += 'x'
        }
        else if (i == 5 & j > 25 & j < 53){
            art += 'x'
        }
        else if (i == 6 & j > 26 & j < 52){
            art += '#'
        }
        else if (i == 7 & j > 26 & j < 30){
            art += '#'
        }
        else if (i == 7 & j > 29 & j < 33){
            art += '.'
        }
        else if (i == 7 & j > 31 & j < 44){
            art += '#'
        }
        else if (i == 7 & j > 43 & j < 46){
            art += '.'
        }
        else if (i == 7 & j > 46 & j < 52){
            art += '#'
        }
        else if (i == 8 & j > 26 & j < 30){
            art += '#'
        }
        else if (i == 8 & j > 29 & j < 33){
            art += '.'
        }
        else if (i == 8 & j > 31 & j < 37){
            art += '#'
        }
        else if (i == 8 & j > 36 & j < 39){
            art += '.'
        }
        else if (i == 8 & j > 39 & j < 44){
            art += '#'
        }
        else if (i == 8 & j > 43 & j < 46){
            art += '.'
        }
        else if (i == 8 & j > 46 & j < 52){
            art += '#'
        }
        else if (i == 9 & j > 26 & j < 37){
            art += '#'
        }
        else if (i == 9 & j > 37 & j < 39){
            art += '.'
        }
        else if (i == 9 & j > 39 & j < 52){
            art += '#'
        }
        else if (i == 10 & j > 26 & j < 37){
            art += '#'
        }
        else if (i == 10 & j > 37 & j < 39){
            art += '.'
        }
        else if (i == 10 & j > 39 & j < 52){
            art += '#'
        }
        else{
            art += '.'
        }
    }
    art += "\n"
}

document.getElementById('houseArt').textContent = art;

