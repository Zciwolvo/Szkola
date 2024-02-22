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
let fullName: string = "John Doe";

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

// Zadanie 4

// Definicja interfejsu Osoba
interface Osoba {
    imie: string;
    nazwisko: string;
    wiek: number;
    email?: string; // Dodatkowe pole opcjonalne
}

// Funkcja wyświetlająca dane osoby zgodnie z interfejsem Osoba
function wyswietlDaneOsoby(osoba: Osoba): void {
    console.log(`Imię: ${osoba.imie}`);
    console.log(`Nazwisko: ${osoba.nazwisko}`);
    console.log(`Wiek: ${osoba.wiek}`);
    if (osoba.email) {
        console.log(`Email: ${osoba.email}`);
    } else {
        console.log('Brak adresu email.');
    }
}

const przykladowaOsoba: Osoba = {
    imie: 'Jan',
    nazwisko: 'Kowalski',
    wiek: 30,
    email: 'jan.kowalski@example.com'
};

wyswietlDaneOsoby(przykladowaOsoba);

// Zadanie 5 i 6

// Definicja klasy Car
class Car {
    make: string;
    model: string;
    year: number;

    constructor(make: string, model: string, year: number) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    displayCarInfo(): void {
        console.log(`Car:`);
        console.log(`   Make: ${this.make}`);
        console.log(`   Model: ${this.model}`);
        console.log(`   Year: ${this.year}`);
    }
}

// Trzy obiekty będące instancjami klasy Car
const car1: Car = new Car('Toyota', 'Corolla', 2020);
const car2: Car = new Car('Ford', 'Mustang', 2018);
const car3: Car = new Car('Honda', 'Civic', 2019);

car1.displayCarInfo();
car2.displayCarInfo();
car3.displayCarInfo();

// Zadanie 7

// Klasa Truck dziedzicząca z klasy Car
class Truck extends Car {
    bedSize: string;

    constructor(make: string, model: string, year: number, bedSize: string) {
        super(make, model, year); // Wywołanie konstruktora klasy Car przy pomocy super
        this.bedSize = bedSize;
    }

    displayTruckInfo(): void {
        super.displayCarInfo(); // Wywołanie metody displayCarInfo() z klasy Car
        console.log(`Bed Size: ${this.bedSize}`);
    }
}

// Przykładowe użycie klasy Truck
const truck1: Truck = new Truck('Ford', 'F-150', 2021, '2 m');
console.log('Truck 1 Info:');
truck1.displayTruckInfo();

// Zadanie 8 (druga część w pliku z8.ts)


import { ExportedCar } from './z8.js'; // Import klasy Car

export class ImportedTruck extends ExportedCar {
    bedSize: string;

    constructor(make: string, model: string, year: number, bedSize: string) {
        super(make, model, year); // Wywołanie konstruktora klasy Car przy pomocy super
        this.bedSize = bedSize;
    }

    displayTruckInfo(): void {
        super.displayCarInfo(); // Wywołanie metody displayCarInfo() z klasy Car
        console.log(`Bed Size: ${this.bedSize}`);
    }
}


// Zadanie 10

// Przykładowa funkcja strzałkowa
const multiply = (a: number, b: number): number => {
    return a * b;
};

// Wywołanie funkcji strzałkowej
const result = multiply(5, 3);
console.log('Wynik mnożenia:', result);

