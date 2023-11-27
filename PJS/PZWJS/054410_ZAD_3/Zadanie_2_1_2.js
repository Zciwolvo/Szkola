"use strict";
exports.__esModule = true;
var car = /** @class */ (function () {
    function car(brand, year, model) {
        this.Brand = brand;
        this.Year = year;
        this.Model = model;
    }
    car.prototype.Result = function () {
        return " \n        Brand: " + this.Brand + "\n        Year: " + this.Year + "\n        Model: " + this.Model;
    };
    return car;
}());
exports.car = car;
var car1 = new car("Audi", 2010, "A1");
var car2 = new car("Opel", 1991, "Astra");
var car3 = new car("Fiat", 1967, "125p");
var car4 = new car("Honda", 1997, "Civic Type R");
console.log(car1.Result());
console.log(car2.Result());
console.log(car3.Result());
console.log(car4.Result());
