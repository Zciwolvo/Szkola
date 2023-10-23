document.getElementById('processFilesButton').addEventListener('click', async () => {
    const fileInput1 = document.getElementById('fileInput1').files[0];
    const fileInput2 = document.getElementById('fileInput2').files[0];

    if (!fileInput1 || !fileInput2) {
        alert('Select two files.');
        return;
    }

    const text1 = await readFileAsync(fileInput1);
    const text2 = await readFileAsync(fileInput2);

    const processedText = processText(text1);

    await saveToFileAsync(processedText, fileInput2.name);

    document.getElementById('result1').textContent = 'Result 1: ' + text1;
    document.getElementById('result2').textContent = 'Result 2: ' + processedText;
});


async function readFileAsync(file) {
    const fileReader = new FileReader();
    return new Promise((resolve, reject) => {
        fileReader.onload = () => {
            resolve(fileReader.result);
        };
        fileReader.readAsText(file);
    });
}

function processText(text) {
    const shift = 3;
    return text.replace(/[a-zA-Z]/g, (char) => {
        let code = char.charCodeAt(0);
        let base = code < 97 ? 65 : 97;
        return String.fromCharCode(((code - base + shift) % 26) + base);
    });
}

async function saveToFileAsync(text, fileName) {
    const blob = new Blob([text], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = fileName;
    a.style.display = 'none';
    document.body.appendChild(a);

    a.click();

    URL.revokeObjectURL(url);
}