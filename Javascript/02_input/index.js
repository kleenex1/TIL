const myTextInput = document.querySelector('#my-text-input');
const myPtag = document.querySelector('#my-paragraph');

function inputText(a) {
  myPtag.innerText = a.target.value
};

myTextInput.addEventListener('input', inputText);