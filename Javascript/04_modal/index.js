const modalContent = document.querySelector('#modal-content')
const modalBtn = document.querySelector('#modal-btn')
const modalCancelBtn = document.querySelector('#modal-cancel-btn')
const modalOverlay = document.querySelector('#modal-content')

function modalToggle(event) {
  modalContent.classList.toggle('active')
  event.stopPropagation();
}

modalBtn.addEventListener('click', modalToggle)
modalCancelBtn.addEventListener('click', modalToggle)
modalOverlay.addEventListener('click', modalToggle)
