"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
exports.__esModule = true;
var Zadanie_2_1_2_1 = require("./Zadanie_2_1_2");
var Truck = /** @class */ (function (_super) {
    __extends(Truck, _super);
    function Truck(Brand, Year, Model) {
        return _super.call(this, Brand, Year, Model) || this;
    }
    return Truck;
}(Zadanie_2_1_2_1.car));
exports.Truck = Truck;
var truck = new Truck("Hyundai", 2007, "i30");
console.log(truck.Result());
