export class ExportedCar {
    make: string;
    model: string;
    year: number;

    constructor(make: string, model: string, year: number) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    displayCarInfo(): void {
        console.log(`Make: ${this.make}`);
        console.log(`Model: ${this.model}`);
        console.log(`Year: ${this.year}`);
    }

    getCarDescription(): string {
        return `${this.year} ${this.make} ${this.model}`;
    }
}