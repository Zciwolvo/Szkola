function displayListAsynchronously(listItems, container) {
    const tick = (index) => {
        if (index < listItems.length) {
            const listItem = document.createElement('li');
            listItem.textContent = listItems[index];
            container.appendChild(listItem);

            setTimeout(() => {
                tick(index + 1);
            }, 1000);
        }
    };

    tick(0);
}

function displayArrayContentsAsynchronously(array, container, index = 0) {
    if (index < array.length) {
        const element = document.createElement('div');
        element.textContent = array[index];
        container.appendChild(element);

        setTimeout(() => {
            displayArrayContentsAsynchronously(array, container, index + 1);
        }, 1000);
    }
}

const listItems = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'];
const listContainer = document.getElementById('list');

const arrayContents = ['Element 1', 'Element 2', 'Element 3', 'Element 4', 'Element 5'];
const arrayContainer = document.getElementById('arrayContents');

displayListAsynchronously(listItems, listContainer);
displayArrayContentsAsynchronously(arrayContents, arrayContainer);
