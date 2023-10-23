document.getElementById('loadDataButton').addEventListener('click', async () => {
    const dataContainer = document.getElementById('dataContainer');
    dataContainer.innerHTML = 'Loading...';

    try {
        const serverData = await fetchDataFromServer();
        const browserData = await fetchDataFromBrowser();

        dataContainer.innerHTML = `
            <p>Server Data: ${serverData}</p>
            <p>Browser Data: ${browserData}</p>
        `;
    } catch (error) {
        dataContainer.innerHTML = `Error: ${error.message}`;
    }
});

async function fetchDataFromServer() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const serverResponse = 'Server data received';
            resolve(serverResponse);
        }, 2000);
    });
}

async function fetchDataFromBrowser() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const browserResponse = 'Browser data processed';
            resolve(browserResponse);
        }, 1000);
    });
}