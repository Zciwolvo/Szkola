var text = ['jakiś', 'tekst', 'nie', 'do', 'końca', 'normalny',]
var i;

for (i=0; i<text.length; i++)
{
    process.nextTick(function(i)
    {
        console.log(text[i])
    }, i)
}