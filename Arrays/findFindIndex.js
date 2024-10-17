
// Los métodos .find() y .findIndex() iteran sobre los arrays pero NO MODIFICAN el array original (Inmutability)

//1. Método .find(): Devuelve el primer elemento de un array que cumpla con la condición dada

console.log('Método .find() y .findIndex(), ejemplo 1: ')
const multipleOf5 = [5, 10, 15, 20]
const greaterThan10 = multipleOf5.find(number => number > 10) // Devuelve el primer elemento mayor que 10
const greaterThan10Ind = multipleOf5.findIndex(number => number > 10 ) // Devuelve LA POSICIÓN del primer elemento mayor que 10

console.log(multipleOf5)
console.log(greaterThan10)
console.log(greaterThan10Ind) // Recuerda que los elementos de un array comienzan a contarse desde cero
