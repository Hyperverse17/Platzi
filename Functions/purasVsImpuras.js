// Funciones puras: Siempre dan una misma salida a una misma entrada, además no producen side effects:

// Side Effects
// 1. Modificar variables globales
// 2. Modificar parÃ¡metros
// 3. Solicitudes HTTP
// 4. Imprimir mensajes en pantalla o consola
// 5. ManipulaciÃ³n del DOM
// 6. Obtener la hora actual

// Ejemplo función pura
function sum (a, b) {
    return a + b
  }
  
// Funciones impuras  
function sum (a, b) {
    console.log('A: ', a) // Una impresión en pantalla es considerado un Side Effect
    return a + b
    }
  
// Ejemplo de una función impura
  let total = 0 // Variable glogal
  function sumWithSideEffect (a) {
    total += a // La modificación de una variable global es un side effect
    return total
  }
  
  // Ejemplo de función pura 2
  function square(x) {
    return x * x
  }
  
// Ejemplo de función pura 3
  function addTen (y) {
    return y + 10
  }
  
  const number = 5
  const finalResut = addTen(square(number)) // Las funciones compuestas o anidadas también pueden ser funciones puras
  console.log(finalResut)