
// Otra forma de crear objetos es instanciándolos a partir de un "molde" o clase. El molde lleva los elementos mímimos para crearlo
// Para definir este molde:

function Persona(nombre, apellido, edad){ // elementos minimos
    this.nombre = nombre // uso de la palabra reservada this (equivalente al self de Python)
    this.apellido = apellido
    this.edad = edad
}

// Para instanciar se usa la palabra reservada new

const Heidi = new Persona("Heidi", "Galicia", 10)
const Lola = new Persona("Lola", "Galicia", 8)

// De igual forma es posible agregar nuevas propiedades

Heidi.direccion = { // De esta forma se agregan propiedades a instancias existentes
    calle:"Canalito",
    numExt: 159,
    numInt: 204
}

console.log(Heidi.direccion.calle)
// console.log(Lola.direccion.calle) // marca error

// El Prototype sirve para agregar propiedades y métodos a la clase y por ende a todas las instancias creadas

Persona.prototype.nacionalidad = "Mexicana" // Asigna esta propiedad a todas las instancias de esta clase

console.log(Heidi.nacionalidad)
console.log(Lola.nacionalidad)

Persona.prototype.saludar = function(name) {
    console.log("Hola,",name,"mi nombre es",this.nombre) // se usa this para hacer referencia a los atributos de la instancia
}

Heidi.saludar("Valeria")
Lola.saludar("Jovani")
