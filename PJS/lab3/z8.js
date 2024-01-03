"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ExportedCar = void 0;
var ExportedCar = /** @class */ (function () {
    function ExportedCar(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }
    ExportedCar.prototype.displayCarInfo = function () {
        console.log("Make: ".concat(this.make));
        console.log("Model: ".concat(this.model));
        console.log("Year: ".concat(this.year));
    };
    ExportedCar.prototype.getCarDescription = function () {
        return "".concat(this.year, " ").concat(this.make, " ").concat(this.model);
    };
    return ExportedCar;
}());
exports.ExportedCar = ExportedCar;
