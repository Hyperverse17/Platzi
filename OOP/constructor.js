
// Otra forma de crear objetos es instanciándolos a partir de un "molde" o clase. El molde lleva los elementos mímimos para crearlo
// Para definir este molde:

function Persona(nombre, apellido, edad){ // elementos minimos
    this.nombre = nombre // uso de la palabra reservada this (equivalente al self de Python)
    this.apellido = apellido
    this.edad = edad
}

// Para instanciar se usa la palabra reservada new

const Heidi = new Persona("Heidi", "Galicia", 10)

// De igual forma es posible agregar nuevas propiedades

Heidi.direccion = {
    calle:"Canalito",
    numExt: 159,
    numInt: 204
}

console.log(Heidi.direccion.calle)

// Prototype
