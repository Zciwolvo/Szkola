function delay(milliseconds: number, count: number): Promise<number> {
    return new Promise<number>(resolve => {
            setTimeout(() => {
                resolve(count);
            }, milliseconds);
        });
}
async function HelloWorld(): Promise<void> {
    console.log("Hello");

    for (let i = 0; i < 10; i++) {
        const count: number = await delay(500, i);
        console.log(count);
    }

    console.log("Hello World!");
}
HelloWorld();