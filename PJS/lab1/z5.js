let peopleJSON = '[{"name": "John", "age": 30},{"name": "Alice", "age": 25},{"name": "Bob", "age": 35}]';

const people = JSON.parse(peopleJSON);

function displayPeople() {
    const peopleList = document.getElementById('peopleList');
    peopleList.innerHTML = '';

    for (const person of people) {
        const listItem = document.createElement('li');
        listItem.textContent = `Imię: ${person.name}, Wiek: ${person.age}`;
        peopleList.appendChild(listItem);
    }
}

const addPersonButton = document.getElementById('addPersonButton');
addPersonButton.addEventListener('click', () => {
    const newPersonName = document.getElementById('newPersonName').value;
    const newPersonAge = document.getElementById('newPersonAge').value;

    if (newPersonName && newPersonAge) {
        const newPerson = { name: newPersonName, age: parseInt(newPersonAge) };
        people.push(newPerson);

        displayPeople();

        const updatedJSON = JSON.stringify(people);
        document.getElementById('jsonText').textContent = updatedJSON;
    }
});

displayPeople();
document.getElementById('jsonText').textContent = peopleJSON;
