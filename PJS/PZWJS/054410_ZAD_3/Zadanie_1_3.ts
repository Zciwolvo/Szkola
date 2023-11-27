let bool :boolean= true;
var string:string="string";
var numer:number=98;

enum Enum {enum1,enum2,enum3,enum4};

var useZm :Enum= Enum.enum1;
var useZm :Enum = Enum.enum2;
var useZm :Enum = Enum.enum3;
var useZm :Enum = Enum.enum4;

let Array_All:[number,string,string,string];


var zmAny:any[]= [true,40,"kot","pies"];

var zwyklyArray:number[]=[1,2,3,4,5];

type Union = Array<string|number>;
let zmUnion1_str : Union = ["a","b","c"];
let zmUnion2_num : Union = [3,2,1,4,5,6];

function voidFunction() : void {
    console.log('void()');
}