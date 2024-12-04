
// Capacidades que tienen las funciones al igual que otros objetos

// 1. Pasar funciones como argumentos -> se conoce como Callback

function a () {}
function b (a) {}
b(a)

// 2. Retornar funciones

function a () {
  function b () {}
  return b
}

// Asignar funciones a variables -> Se conoce como expresión de función

const constant1 = function () {} // Es una forma distinta de declarar funciones

// Tener propiedades y métodos

function a () {}
const obj = {} // De esta forma se declara un objeto
a.call(obj)

// Anidar funciones -> Nested functions

function a () {
  function b () {
    function c () {
        // code
    }
    c() // llamado dentro de la función
  }
  b()
}
a()

// ¿Es posible almacenar funciones en objetos? R: Sí

const rocket = {
  name: 'Falcon 9', // Propiedades del objeto rocket
  launchMessage: function launchMessage () {
    console.log('💥🚀')
  }
}

rocket.launchMessage()

// Más emojis en: https://emojikeyboard.io/