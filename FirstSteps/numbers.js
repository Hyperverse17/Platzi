
// Para estas variables numéricas se usará la palabra reservada const en vez de let

const entero = 42 // Entero
const decimal = 3.1416 // Decimal

// Const no distingue entre enteros y decimales, de hecho la función typeof nos regresa number para ambos
console.log(typeof entero,typeof decimal) // typeof regresa el tipo de variable 

const cientifico=5e3 // Notación científica, ejemplo de 5 x 10 ^3

// Casos especiales
const infinito=Infinity // Representación de infinito
const noEsUnNumero=NaN // Representación de un Not a Number 

// Operaciones aritméticas
const suma = 3 + 4
console.log(suma)
const resta = 4 - 4
const mutiplicacion = 4 * 7
const division = 16 / 2
const modulo = 15 % 8
const exponenciacion = 2 ** 3

console.log(10+7) // Es posible ingresar operaciones aritméticas dentro del console log, aunque estas no se asignarán a ninguna variable

// Consideraciones: JavaScript no es un lenguaje recomendable para cálculos numéricos ya que su precisión no es muy buena.
// Por ejemplo, al sumar 0.1 + 0.2 nos regresa 0.30000000000000004
const resultado = 0.1 + 0.2
console.log(resultado)
// Esta impresición se puede "arreglar", dándole formato a la operación
console.log(resultado.toFixed(1)) // .toFixed(n) sirve para representar un número con n decimales

// Sin embargo este "arreglo" es únicamente visual, ya que al comparar los resultados con "===", nos regresa false
console.log(resultado===0.3) // "===" sirve para comparar tanto VALOR como TIPO

// Para hacer operaciones más avanzadas, se usa el módulo Math
const raizCuadrada = Math.sqrt(16)
const valorAbsoluto = Math.abs(-7)
const aleatorio = Math.random() // Regresa un número aleatorio entre 0 y 1 uniformememnte distribuido

console.log(raizCuadrada)
console.log(valorAbsoluto)
console.log(aleatorio)

//////////////////
// Cuál es la diferencia entre const y let???
console.log("--- Prueba con let ---")
let a1 = 0.1
let b1 = 0.2
let c1 = a1+b1
console.log(c1)
let d1 = c1.toFixed(1)
console.log(d1)
console.log(d1 === 0.3)

console.log("--- Prueba con const ---")
const a2 = 0.1
const b2 = 0.2
const c2 = a2+b2
console.log(c2)
const d2 = c2.toFixed(1)
console.log(d2)
console.log(d2 === 0.3)
