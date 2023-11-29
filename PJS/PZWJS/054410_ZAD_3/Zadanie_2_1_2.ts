export class car {
    Brand:string;
    Year:number;
    Model:string;
    
    constructor(brand:string, year:number, model:string){
    this.Brand = brand;
    this.Year = year;
    this.Model = model
    }
    Result(): string {
        return ` 
        Brand: ${this.Brand}
        Year: ${this.Year}
        Model: ${this.Model}`;
    }
}

let car1 = new car("Audi", 2010, "A1");
let car2 = new car("Opel", 1991, "Astra");
let car3 = new car("Fiat", 1967, "125p");
let car4 = new car("Honda",1997,"Civic Type R")
console.log(car1.Result())
console.log(car2.Result())
console.log(car3.Result())
console.log(car4.Result())