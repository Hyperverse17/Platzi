
// Map y Foreach iteran sobre los arrays pero NO MODIFICAN el array original

// El método .map toma cada elemento de un array y le aplica alguna función definida por el usuario, retorna cada elemento después de aplicarle la función en un nuevo array
// 1. Ejemplo de .map()

const numbers = [1, 2, 3, 4, 5]
const squaredNumbers = numbers.map(num => num * num) // el primer num es el nombre que se le dará a cada elemento del array durante la iteración. Nótese el uso de una arrow function

console.log(numbers)
console.log(squaredNumbers)

// El método .forEach() toma cada elemento del array y le aplica alguna función definida por el usuario, devuelve sólo el valor de la evaluación en cada iteración

const colors = ['red', 'pink', 'blue']
const iteratedColors = colors.forEach(color => console.log(color)) // Esta función solo barre e imprime en pantalla cada elemento del array

console.log(colors)
console.log(iteratedColors) // Nótese que esta linea regresa undefined, puesto que no se ha creado algún nuevo array o elemento 

// Ejemplos de aplicación

// 1. Conversión de grados farenheit a Celcius: .map() 

const temperaturesInFahrenheit = [32, 68, 95, 104, 212]
const temperaturesInCelsius = temperaturesInFahrenheit.map(fahrenheit => (5/9) * (fahrenheit - 32))

console.log('Arreglo Fahrenheit: ', temperaturesInFahrenheit)
console.log('Arreglo Celsius: ', temperaturesInCelsius)

// 2. suma de todos los elementos de un array: .forEach()

const newNumbers = [1, 2, 3, 4, 5]
let sum = 0 // Inicialización de la variable que guardará el resultado

newNumbers.forEach(number => { // funciones más complejas es posible definirlas en varias líneas usando llaves {}
  sum += number
})

console.log('Array of Numbers: ', newNumbers)
console.log('Sum of Numbers: ', sum)
