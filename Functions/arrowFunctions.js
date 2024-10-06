
/* Las Arrow Function son útiles porque permiten:

1. Escribir métodos más concisos
2. Simplificar una línea de código para que sea más legible
3. Aprovechar las características de retorno implícito y el no uso de paréntesis
4. Olvidarse de manejar el contexto this
5. Definir de manera compacta una función convencional
6. Eliminar las llaves y la palabra return si la función tiene solamente una sentencia que devuelve un valor
7. Reducir el código aún más utilizando parámetros */



const greeting = function(name){ // Ejemplo Función tradicional
    return `Hi, ${name}`
}

const newGreeting = (name) => {return `Hi, ${name}`} // Ejemplo Arrow Function Explícita (por el uso del  return). Nótese la ausenciia de la palabra reservada function


const newGreetingImplicit = name => `Hi, ${name}` // Ejemplo de una arrow function implícita (No hay return como tal). Nótese que cuando sólo hay un parámetro de entrada, es posible prescindir de los paréntesis
const newGreetingImplicitWithTwoParameters=(name,lastName)=>`Hi, I'm ${name} ${lastName}` // Cuando hay más de un parámetro de entrada, se colocan entre paréntesis

// Lexical Binding
const fictionalCharacter = {
    name:'Uncle Ben',
    messageWithTraditionalFunction : function(message){
        console.log(`${this.name} says: ${message}`) //Nótese el uso de this
    },
    messageWithArrowFunction : (message)=>{console.log(`${this.name} says: ${message}`)}}

fictionalCharacter.messageWithTraditionalFunction('With great power comes great responsability.')
fictionalCharacter.messageWithArrowFunction('Beware of Doctor Octopus.') // A pesar de que en la construcción igual se usó this, al ejecutar, en pantalla aparece "undefined" NO existe una vinculación

//Cuando se usa una función flecha como método de un objeto, el this dentro de la función flecha no apunta al objeto que invocó el método. En cambio, el valor de this se hereda del contexto de ejecución en el que se definió la función flecha. Esto significa que this se refiere al this del entorno circundante (en el que se creó la función), y no puede ser cambiado con métodos como call, apply o bind.

//O sea en este ejemplo this de la arrow function apunta al objeto global window.