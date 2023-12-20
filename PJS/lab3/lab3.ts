const hello: string = "Hello";
const world: any = "World"
console.log(`${hello} ${world} !`);

// Zadanie 1

var counterVar = 0;
let counterLet = 0;

function Counter(a: number) {
    return a += 1
  }

counterVar = Counter(counterVar)
counterLet = Counter(counterLet)
console.log(counterVar, counterLet)

// Zadanie 2

function Suma(...a: number[]) {
    return [...a].reduce((acc, val) => acc + val, 0);
}

console.log(Suma(1,6,4,3));

// Zadanie 3

// Number variable
let age: number = 25;

// String variable
let name: string = "John Doe";

// Boolean variable
let isActive: boolean = true;

// Array of numbers
let numbers: number[] = [1, 2, 3, 4, 5];

// Tuple
let person: [string, number] = ["John", 30];

// Union type
let petType: string | number = "Dog";

// Any type
let data: any = 10;

// Null or undefined
let value: number | null | undefined = null;

// Void type
function greet(): void {
    console.log("Hello!");
}


