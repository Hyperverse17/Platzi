
// Operadores lógicos en JS

const a = 10
const b = 7
let c   = "10"
let d   = "10"

console.log("--- Operadores Lógicos ---")
console.log(a>b) // Estrictamente mayor que
console.log(a>=b) // Mayor o igual que
console.log(a<b) // Estrictamente menor que
console.log(a<b) // Menor o igual que
console.log(a==b) // Estrictamente igual en VALOR
console.log(a!=b) // Distinto en VALOR
console.log(c===d) // Estrictamente igual en VALOR y TIPO
console.log(c!==d) // Distinto en VALOR y TIPO

// Operadores relacionales

// tenemos && (and), || (or) y ! (not)
// ! ya se usó en la sección anterior, sirve para negar por ejemplo != (no igual o distinto)
console.log() // imprime un salto de línea
const A = 17
const B = 21
const C = "string"

console.log("---Operadores Relacionales---")
console.log((A < B) && (B != C))
console.log(!((A > B) || (B == C))) // Normalmente regresaría false porque ni A es mayor que B ni B es igual a C, pero como tiene una negación al inicio, el false es cambiado por true
