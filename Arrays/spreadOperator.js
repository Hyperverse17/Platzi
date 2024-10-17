
// El spread operator, se representa con tres puntos seguidos ... y puede utilizarse para:

// 1. Copiar un Array

const originalArray = [1, 2, 3, 4, 5]
const copyOfAnArray = [...originalArray]

console.log(originalArray)
console.log(copyOfAnArray)

// 2. Combinar Arrrays

const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const combinedArray = [...array1, ...array2]

console.log(array1)
console.log(array2)
console.log(combinedArray)

// 3. Crear nuevos arrays a partir de otros y agregarle nuevos elementos

const baseArray = [1, 2, 3]
const arrayWithAdditionalElements = [...baseArray, 4, 5, 6]

console.log(baseArray)
console.log(arrayWithAdditionalElements)

// 4. Pasar argumentos a una función que recibe varios

function sum (a, b, c, d, e, f) {
  return a + b + c + d + e + f
}

const numbers = [1, 2, 3, 4, 5, 6]
const result = sum(...numbers) // en vez de pasarlos directamente como sum(1,2,3,4,5,6)

console.log(result)