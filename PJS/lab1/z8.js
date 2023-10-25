
var alpha = Array.from(Array(26)).map((e, i) => i + 65);
var alphabet = alpha.map((x) => String.fromCharCode(x));
var vovels = ["A", "O", "U", "E", "I", "Y"]
var i = 0

const elapsedTimeContainer = document.getElementById('elapsedTime');
const letterAContainer = document.getElementById('letterA');
const alphabetContainer = document.getElementById('alphabet');

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

//Zadanie 8.1
async function countTime() {
    var time = 1
    while (true){
        await sleep(1000);
        elapsedTimeContainer.textContent = time; 
        time += 1;
    }
    
}

//Zadanie 8.2
async function addA() {
    while (true){
        await sleep(1000);
        for (let index = 0; index < 5; index++) {
            letterAContainer.textContent += "a"
            await sleep(10);
        }   
    }

}

//Zadania 8.3
async function LogLetter() {
    while (true){
        if (vovels.includes(alphabet[i])) {
            alphabetContainer.textContent = alphabet[i];
            await sleep(2000);
        } else {
            alphabetContainer.textContent = alphabet[i];
            await sleep(500);
        }
        if (i < alphabet.length){
            i += 1;
        } else{
            i = 0;
        }
    }

}

countTime();
addA();
LogLetter();

