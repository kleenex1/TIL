// console.log('Hello')

// console.log('4'+3);
// console.log('4'-3);
// console.log('함수 호출 후');

// console.log(NaN -1);


// const fruits = ['딸기','바나나']

// for (let fruit in fruits) {
//   console.log(fruits[fruit])
// }

// const spreadOpr = function(agr1, agr2) {
//   return agr1 + agr2
// }

// const number = [29,30]
// console.log(spreadOpr(number))

// const numbers = [1,2,3,4,5]

// const oddNums = numbers.filter((num, index) => {return num %2})

// console.log(oddNums)

const num = [1,2,3]
const result = num.reduce((acc,num) => {return acc+num}, 10)
console.log(result)