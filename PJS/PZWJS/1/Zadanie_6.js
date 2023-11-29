function wy(el, callback)
{
    console.log(el);
    if (tab.lenght){
        process.nextTick(function(){
            callback();
        });
    }
}

function main(tab){
    var el = tab.shift();
    wy(el,function(){
        main(tab);
    });
}

var tab = ['jakiś', 'tekst', 'nie', 'do', 'końca', 
'normalny','jakiś', 'tekst', 'nie', 'do', 'końca', 'normalny']

main(tab);