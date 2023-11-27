/*  Co jedną sekundę pięd razy wyświetlana litera
‘a’ co 10 ms */
function main(){
    var l = 0;
    function display(){
        if(l<5){
        console.log("a");
        l++;
        } else{
            clearInterval(inter);
        }
    }
    var inter = setInterval(display, 10);
}

var inter2 = setInterval(main, 1000);