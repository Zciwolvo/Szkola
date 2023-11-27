import { car } from "./Zadanie_2_1_2";

export class Truck extends car {
    constructor(Brand:string, Year:number, Model:string) {
        super(Brand, Year, Model);
    }
}

let truck = new Truck("Hyundai", 2007, "i30");

console.log(truck.Result());