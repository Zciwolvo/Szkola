function Sum() {
    var attributes = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        attributes[_i] = arguments[_i];
    }
    var i = 0;
    for (var _a = 0, attributes_1 = attributes; _a < attributes_1.length; _a++) {
        var attribute = attributes_1[_a];
        i += attribute;
    }
    console.log(i);
}
console.log("Sum(2): ");
Sum(2);
console.log("Sum(3,4): ");
Sum(3, 4);
console.log("Sum(1,2,3): ");
Sum(1, 2, 3);
