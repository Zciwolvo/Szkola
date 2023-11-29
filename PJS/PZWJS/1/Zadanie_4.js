var alfabet = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "c", "b", "n", "m"];
var samogloska = ["a", "e", "i", "y", "o", "u"];
var l = 0;
var i;
var end;
var interval = setInterval(display, 500);

function chceck(){
    for (i=0; i<samogloska.length; i++)
    {
        if (alfabet[l]==samogloska[i])
        {
            return true;
        }
    }
}

function display()
{
    console.log(alfabet[l]);
    if(chceck())
    {
        clearInterval(interval);
        end = setTimeout(function()
            {
                l++;
                interval=setInterval(display, 500);
                clearTimeout(end);
            }
        ,2000)
    }else {l++;}
}  if(l>=alfabet.length){
    clearInterval(interval);
}