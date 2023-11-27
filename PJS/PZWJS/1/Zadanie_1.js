/*  Za pomocą liczników wykonaj zdarzenie
wyświetlania liczby sekund co 1 sekundę od
uruchomienia */
var s=1;
function waitFunc(){
    console.log(s);
    s=s+1;
}

setInterval(waitFunc,1000);
