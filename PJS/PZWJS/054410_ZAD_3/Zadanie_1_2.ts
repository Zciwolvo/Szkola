function Sum(...attributes: number[]) {
	let i:number=0
	for (let attribute of attributes) {
		i+=attribute
	}
	console.log(i);
}
console.log("Sum(2): ");
Sum(2)
console.log("Sum(3,4): ");
Sum(3,4)
console.log("Sum(1,2,3): ");
Sum(1,2,3)