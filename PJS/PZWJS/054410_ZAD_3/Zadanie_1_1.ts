var numberVar: number = 0;
let numberLet: number = 0;

function counterVar() {
    numberVar++;
    console.log(`Value Var: ${numberVar}`)
}
function counterLet() {
    numberLet++;
    console.log(`Value Let: ${numberLet}`)
}
setInterval(counterVar, 500);
setInterval(counterLet, 500);