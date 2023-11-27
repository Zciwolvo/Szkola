function show(user) {
    return "Name: " + user.Name + "Lastname: " + user.LastName + "Nationality: " + user.Nationality;
}
var user = { Name: "Jan\n", LastName: "Kowalski\n", Nationality: "Polish" };
console.log(show(user));
