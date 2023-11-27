interface Person {
    Name:string;
    LastName:string;
    Nationality:string;
}
function show(user:Person):string{
    return "Name: "+user.Name+"Lastname: "+user.LastName+"Nationality: "+user.Nationality;
}
var user = {Name:"Jan\n",LastName:"Kowalski\n",Nationality:"Polish"}

console.log(show(user));