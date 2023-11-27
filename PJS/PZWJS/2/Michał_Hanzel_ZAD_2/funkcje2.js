const fs = require('fs');
var express = require('express');
var app = express();
var path = require('path');

var cars = JSON.parse(fs.readFileSync('./CRUD/car.json', 'utf8'));
var car = function (id, brand, model, year) {
    return { id: id, brand: brand, model: model, year: year };
}

var writeJson = () => fs.writeFile("./CRUD/car.json", JSON.stringify(cars), 'utf8', function (err) {
    if (err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});

app.use(express.urlencoded({
    extended: true
}));

app.get('/car', function (req, res) {
    res.sendFile(path.join(__dirname, 'CRUD/index.html'));

    console.log("Cookies: ", req.cookies);
    info = "już tu byłem";
    if (typeof req.cookies === "undefined") {
        console.log("Unrecognized cookie")
    }
    else {
        if (!req.cookies.hasVisited) {
            res.cookie('hasVisited', "1", { maxAge: 60 * 60 * 1000, httpOnly: true, path: '/' });
            info = "mój pierwszy raz";
        }
        res.send(info);
    }
});

app.post('/car', function (req, res, next) {
    var id = req.body.id;
    var brand = req.body.brand;
    var model = req.body.model;
    var year = req.body.year;
    cars.push(car(id, brand, model, year));
    console.log("Added: id: " + cars.slice(-1)[0].id + " | brand: " + cars.slice(-1)[0].brand + " | model: " + cars.slice(-1)[0].model + " | year: " + cars.slice(-1)[0].year);
    writeJson();

});

app.post('/car/:id', function (req, res, next) {
    var id = req.body.id;
    let found = cars.find(function (item) {
        return item.id === id;
    });

    if (found) {

        let targetIndex = cars.indexOf(found);
        console.log("Removed: id: " + cars[targetIndex].id + " | brand: " + cars[targetIndex].brand + " | model: " + cars[targetIndex].model + " | year: " + cars[targetIndex].year);
        cars.splice(targetIndex, 1);
        writeJson();
    }
});

app.listen(8080);
console.log('Listening on port 8080');