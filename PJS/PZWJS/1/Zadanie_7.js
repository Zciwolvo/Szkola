var zp = require('zp');
var text = '{"person1":{"name": "Andrzej","surname": "Kowalski","age": 30},"person2":{"name": "Maciej","surname": "Kowalski","age": 43},"person3":{"name": "Andrzej","surname": "Nowak","age": 10}}'
var content = zp.readFileSync('baza.json', 'utf8');
var con1 = JSON.parse(text);
var con2 = JSON.parse(content);

con1.user = {name: 'Andrzej', surname: 'Kowalski', age: 30};

function display()
{
    for(var i in con1)
    {
        console.log(obj[i]);
    }
}

display();
con1.user = {name: 'Maciej', surname: 'Kowalski', age: 43};
var string = JSON.stringify(con1);
