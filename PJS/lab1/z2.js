var time = 0
var alpha = Array.from(Array(26)).map((e, i) => i + 65);
var alphabet = alpha.map((x) => String.fromCharCode(x));
var vovels = ["A", "O", "U", "E", "I"]
var i = 0

//Zadanie 2.1
function CountTime() {
    time += 1
    console.log(time, " seconds has passed.");
}

//Zadanie 2.2
function LogMessageInterval() {
    for (let index = 0; index < 5; index++) {
        setTimeout(console.log("a"), 10)
    }
}

//Zadania 2.3
async function LogLetter() {
    if (vovels.includes(alphabet[i])) {
        console.log(alphabet[i])
        await new Promise(r => setTimeout(r, 2000));
    } else {
        console.log(alphabet[i])
    }
    i += 1
}