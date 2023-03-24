const form = document.querySelector('#input-form');
const resultDiv = document.querySelector('#result');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const num1 = document.querySelector('#num1').value;
    const num2 = document.querySelector('#num2').value;
    const num3 = document.querySelector('#num3').value;
    const num4 = document.querySelector('#num4').value;

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/calculate');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = () => {
        const result = JSON.parse(xhr.responseText).result;
        resultDiv.innerHTML = `Result: ${result}`;
    };
    xhr.send(JSON.stringify({num1: num1, num2: num2, num3: num3, num4: num4}));
});
