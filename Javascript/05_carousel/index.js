// const prevBtn = document.querySelector('#prevBtn')
// const currentElement = document.querySelector('.active')
// const items = document.querySelectorAll('.carousel-item')
// const idx = [...items].indexOf(currentElement)
// const nextBtn = document.querySelector('#nextBtn')

// function preBtn() {
//   console.log(currentElement, items, idx)
//   currentElement.classList.toggle('active')
//   items[((idx-1)+items.length)%items.length].classList.toggle('active')
// }

// function nexBtn() {
//   console.log(currentElement, items, idx)
//   currentElement.classList.toggle('active')
//   items[(idx+1)%items.length].classList.toggle('active')
// }

// prevBtn.addEventListener('click', preBtn)
// nextBtn.addEventListener('click', nexBtn)

// setInterval(function() {
//   const nextBtn = document.querySelector('#nextBtn')
//   nextBtn.click()
// }, 10000)

// document.addEventListener('load', function() {

// })

const prevBtn = document.querySelector('#prevBtn')
prevBtn.addEventListener('click', function() {
  // 지금 active인 것은 어떻게 알죠?
  const currentElement = document.querySelector('.active')
  // 전체 item 중에....... 이 Element의 인덱스?
  const items = document.querySelectorAll('.carousel-item')
  const idx = [...items].indexOf(currentElement)
  console.log(currentElement, items, idx)
  currentElement.classList.toggle('active')
  items[(items.length+idx-1)%items.length].classList.toggle('active')
})

const nextBtn = document.querySelector('#nextBtn')
nextBtn.addEventListener('click', function() {
  // 지금 active인 것은 어떻게 알죠?
  const currentElement = document.querySelector('.active')
  // 전체 item 중에....... 이 Element의 인덱스?
  const items = document.querySelectorAll('.carousel-item')
  const idx = [...items].indexOf(currentElement)
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