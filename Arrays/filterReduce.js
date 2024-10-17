
// Filter y reduce iteran sobre los arrays pero NO MODIFICAN el array original (Inmutability)

//1. Método .filter(): crea un nuevo arreglo sólo con los elementos del arreglo original que cumplen la condición dada

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const evenNumbers = numbers.filter(number => number % 2 == 0) // de esta forma se filtran numeros pares. Nótese que js interpreta por defecto que asignará considerará cada elemento sólo si el resultado de la comparación se cumple
const oddNumbers = numbers.filter(number => number % 2 != 0) // se consideran sólo los elementos que cumplen la condición

console.log()
console.log('Método .filter() Ejemplo 1 con: ',numbers)
console.log('Pares: ',evenNumbers)
console.log('impares: ',oddNumbers)

// 2. Método .reduce(), ejemplo A
const numbersReduce = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log()
console.log('Método .reduce() Ejemplo A con: ',numbersReduce)

// .reduce() recibe tres parámetros: accumulator, current e inicializador
const sum = numbersReduce.reduce((accumulator, currentValue) => accumulator + currentValue, 0) // accumulator se inicializa en cero y se le va a gregando cada current value

console.log('Array original: ',numbersReduce)
console.log('resultado: ',sum) // Resultado de (para este ejemplo) la suma

// 3. Método .reduce(), ejemplo B
const words = ['apple', 'Hello', 'music','bye', 'banana', 'hello', 'bye', 'banana', 'bye', 'bye']
console.log()
console.log('Método .reduce() Ejemplo B con: ',words)

const wordFrecuency = words.reduce((accumulator, currentValue) => { // current value toma el valor de cada elemento del array en cada iteración
// para este ejemplo accumulator pas a ser un OBJETO que va a guardar distintos elementos y características dentro
  if (accumulator[currentValue]) { // Si el elemento de accumulator en la posición current value ya existe, entonces...
    accumulator[currentValue]++ // suma 1
  } else { // si el elemento de accumulator en la posocipon current value no existe y es la primera vez que aparece, entonces inicializa en uno
    accumulator[currentValue] = 1
  }
  return accumulator // retorna el acumulador que esta vez es un objeto
}, {}) // con ",{}" estamos indicando que el objeto inicial es un objeto vacio

console.log(wordFrecuency)

/*/ Exercise: Passing Grade Average

const grades = [85, 92, 60, 78, 95, 66, 88, 50, 94]

const passingGrades = grades.filter(grade => grade >= 70)

const averagePassingGrade = passingGrades.reduce((sum, grade) => sum + grade, 0) / passingGrades.length

console.log('Original Grades: ', grades)
console.log('Passing Grades: ', passingGrades)
console.log('Average Passing Grade: ', averagePassingGrade)*/