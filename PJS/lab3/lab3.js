"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.ImportedTruck = void 0;
var hello = "Hello";
var world = "World";
console.log("".concat(hello, " ").concat(world, " !"));
// Zadanie 1
var counterVar = 0;
var counterLet = 0;
function Counter(a) {
    return a += 1;
}
counterVar = Counter(counterVar);
counterLet = Counter(counterLet);
console.log(counterVar, counterLet);
// Zadanie 2
function Suma() {
    var a = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        a[_i] = arguments[_i];
    }
    return __spreadArray([], a, true).reduce(function (acc, val) { return acc + val; }, 0);
}
console.log(Suma(1, 6, 4, 3));
// Zadanie 3
// Number variable
var age = 25;
// String variable
var fullName = "John Doe";
// Boolean variable
var isActive = true;
// Array of numbers
var numbers = [1, 2, 3, 4, 5];
// Tuple
var person = ["John", 30];
// Union type
var petType = "Dog";
// Any type
var data = 10;
// Null or undefined
var value = null;
// Void type
function greet() {
    console.log("Hello!");
}
// Funkcja wyświetlająca dane osoby zgodnie z interfejsem Osoba
function wyswietlDaneOsoby(osoba) {
    console.log("Imi\u0119: ".concat(osoba.imie));
    console.log("Nazwisko: ".concat(osoba.nazwisko));
    console.log("Wiek: ".concat(osoba.wiek));
    if (osoba.email) {
        console.log("Email: ".concat(osoba.email));
    }
    else {
        console.log('Brak adresu email.');
    }
}
var przykladowaOsoba = {
    imie: 'Jan',
    nazwisko: 'Kowalski',
    wiek: 30,
    email: 'jan.kowalski@example.com'
};
wyswietlDaneOsoby(przykladowaOsoba);
// Zadanie 5 i 6
// Definicja klasy Car
var Car = /** @class */ (function () {
    function Car(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }
    Car.prototype.displayCarInfo = function () {
        console.log("Car:");
        console.log("   Make: ".concat(this.make));
        console.log("   Model: ".concat(this.model));
        console.log("   Year: ".concat(this.year));
    };
    return Car;
}());
// Trzy obiekty będące instancjami klasy Car
var car1 = new Car('Toyota', 'Corolla', 2020);
var car2 = new Car('Ford', 'Mustang', 2018);
var car3 = new Car('Honda', 'Civic', 2019);
car1.displayCarInfo();
car2.displayCarInfo();
car3.displayCarInfo();
// Zadanie 7
// Klasa Truck dziedzicząca z klasy Car
var Truck = /** @class */ (function (_super) {
    __extends(Truck, _super);
    function Truck(make, model, year, bedSize) {
        var _this = _super.call(this, make, model, year) || this; // Wywołanie konstruktora klasy Car przy pomocy super
        _this.bedSize = bedSize;
        return _this;
    }
    Truck.prototype.displayTruckInfo = function () {
        _super.prototype.displayCarInfo.call(this); // Wywołanie metody displayCarInfo() z klasy Car
        console.log("Bed Size: ".concat(this.bedSize));
    };
    return Truck;
}(Car));
// Przykładowe użycie klasy Truck
var truck1 = new Truck('Ford', 'F-150', 2021, '2 m');
console.log('Truck 1 Info:');
truck1.displayTruckInfo();
// Zadanie 8 (druga część w pliku z8.ts)
var z8_js_1 = require("./z8.js"); // Import klasy Car
var ImportedTruck = /** @class */ (function (_super) {
    __extends(ImportedTruck, _super);
    function ImportedTruck(make, model, year, bedSize) {
        var _this = _super.call(this, make, model, year) || this; // Wywołanie konstruktora klasy Car przy pomocy super
        _this.bedSize = bedSize;
        return _this;
    }
    ImportedTruck.prototype.displayTruckInfo = function () {
        _super.prototype.displayCarInfo.call(this); // Wywołanie metody displayCarInfo() z klasy Car
        console.log("Bed Size: ".concat(this.bedSize));
    };
    return ImportedTruck;
}(z8_js_1.ExportedCar));
exports.ImportedTruck = ImportedTruck;
// Zadanie 10
// Przykładowa funkcja strzałkowa
var multiply = function (a, b) {
    return a * b;
};
// Wywołanie funkcji strzałkowej
var result = multiply(5, 3);
console.log('Wynik mnożenia:', result);
