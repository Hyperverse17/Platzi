
// .slice() permite obtener una porción de los elementos de un array. Recibe dos parámetros opcionales: inicio y fin 
const animals=['ant', 'bison', 'spider', 'camel', 'snake', 'duck', 'elephant', 'mouse']

// Ejemplo 1
console.log(animals.slice()) // slice sin parámetros devuelve todo el arreglo original sin alterarlo

// Ejemplo 2
console.log(animals.slice(2)) // En este caso se usa una posición inicial, el resultado será un arreglo desde esa posición hasta el final

// Ejemplo 3
console.log(animals.slice(3,6)) // en este caso se colocan los parámetros de inicio y fin, sin embargo js los interpreta como un intervalo semiabierto [a, b)

// Ejemplo 5
console.log(animals.slice(-2)) // Es posible comenzar el conteo desde atrás, en este caso devuelve el segundo elemento contando desde el final. Aquí no se comienza por cero

// Ejemplo 6
console.log(animals.slice(2,-3)) // De igual forma se comienza a contar desde atrás. de igual forma se trata de un intervalo semiaboerto
