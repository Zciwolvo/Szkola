var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
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
var name = "John Doe";
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
