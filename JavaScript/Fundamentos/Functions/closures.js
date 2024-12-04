
/*En programación, un closure, también conocido como clausura o cierre, es una función que recuerda y tiene acceso al entorno en el que se creó, incluso después de que la función externa que la creó haya terminado de ejecutarse.

En otras palabras, un closure es una función que encapsula un dato (que puede ser una variable o un objeto) y recuerda el estado del entorno en el que se definió. Esto permite que la función interna acceda y utilice variables o valores de la función externa, incluso después de que esta haya finalizado.*/

// Ejemplo # 1
function outerFunction(){
    let outerVariable = "Hello, I am a message from the outer function"
    function innerFunction(){
        console.log(outerVariable) // Tiene acceso a variables que fueron creadas fuera de su contexto
    }
    return innerFunction
}
    
const closureExample = outerFunction() // Se declara la variable closure example como la función outerfunction
closureExample() // La función outer regresa la función inner, por lo que closure example se invoca como una función y esta regresa el mensaje definido en outer function

// Ejemplo # 2
function createCounter(){
    let count = 0
    return function innerCounter(){
        count++
        console.log(count)
    }
}
    
const counterA = createCounter() // Se asigna una variable con una función
console.log("Closure function: Counter A")
counterA() // Después de la asignación, al invocar la "variable-función" va a retornar la función interior y esta a su vez incrementa en uno el valor de la constante definida fuera e imprime el valor en pantalla
counterA() // Misma acción que la línea anterior, sin embargo, sirve de muestra para comprobar que se guarda la información en memoria
counterA()
counterA()

console.log("Closure function: Counter B")
const counterB = createCounter() // Se inicializa otra variable con la misma función
counterB() // Es importante tener cuidado, ya que al reutilizar la función de esta forma la "cuenta" (datos almacenados en memoria), se pierde y se reinicia
counterB()

// Ejemplo 3
console.log("--- Ejemplo 3 ---")
function outerFunction3(){
    let message = "Hello, "
    function innerFunction3(name){
        console.log(message + name)
    }
    return innerFunction3
}
    
const closureA = outerFunction3()
const closureB = outerFunction3()

closureA("Alice") // Ejemplo muy similar a los anteriores. Aquí se visualiza claramente que básicamente es como si se estuviera pasando directamente el argumento "Alice" a la innerFunction3
closureA("Bob")

