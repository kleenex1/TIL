const prevBtn = document.querySelector('#prevBtn')
const currentElement = document.querySelector('.active')
const items = document.querySelectorAll('.carousel-item')
const idx = [...items].indexOf(currentElement)
const nextBtn = document.querySelector('#nextBtn')

prevBtn.addEventListener('click', function() {
  console.log(currentElement, items, idx)
  currentElement.classList.toggle('active')
  items[(items.length+idx-1)%items.length].classList.toggle('active')
})

nextBtn.addEventListener('click', function() {
  console.log(currentElement, items, idx)
  currentElement.classList.toggle('active')
  items[(idx+1)%items.length].classList.toggle('active')
})

setInterval(function() {
    const nextBtn = document.querySelector('#nextBtn')
    nextBtn.click()
  }, 10000)

document.addEventListener('load', function() {

})