var bool = true;
var string = "string";
var numer = 98;
var Enum;
(function (Enum) {
    Enum[Enum["enum1"] = 0] = "enum1";
    Enum[Enum["enum2"] = 1] = "enum2";
    Enum[Enum["enum3"] = 2] = "enum3";
    Enum[Enum["enum4"] = 3] = "enum4";
})(Enum || (Enum = {}));
;
var useZm = Enum.enum1;
var useZm = Enum.enum2;
var useZm = Enum.enum3;
var useZm = Enum.enum4;
var Array_All;
var zmAny = [true, 40, "kot", "pies"];
var zwyklyArray = [1, 2, 3, 4, 5];
var zmUnion1_str = ["a", "b", "c"];
var zmUnion2_num = [3, 2, 1, 4, 5, 6];
function voidFunction() {
    console.log('void()');
}
