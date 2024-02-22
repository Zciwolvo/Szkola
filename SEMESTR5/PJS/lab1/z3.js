 class User {
    constructor(name) {
        this.name = name;
    }

    changeName(newName) {
        this.name = newName;
        this.emitNameChange();
    }

    emitNameChange() {
        const event = new CustomEvent('nameChange', { detail: this.name });
        document.dispatchEvent(event);
    }
}

const userInfo = document.getElementById('userInfo');
const newNameInput = document.getElementById('newNameInput');
const changeNameButton = document.getElementById('changeNameButton');

const user = new User('John');

function updateUserInfo(name) {
    userInfo.textContent = `User Name: ${name}`;
}

changeNameButton.addEventListener('click', () => {
    const newName = newNameInput.value;
    if (newName) {
        user.changeName(newName);
        newNameInput.value = '';
    }
});

document.addEventListener('nameChange', (event) => {
    updateUserInfo(event.detail);
});