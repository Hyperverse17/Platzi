
// Un objeto es básicamente una estructura de datos y posee propiedades con sus respectivos valores
// propiedad: valor
// Los métodos son funciomes que nos permiten interactuar con los objetos
// Se define de la siguiente manera:

const Persona = { // Nótese el uso del = antes de las llaves
    nombre: "Heidi",
    apellido : "Galicia",
    edad: 33,
    estatura: 1.78,
    // Las propiedades pueden a su vez tener subpropiedades
    direccion: { 
        calle: "Canalito", // Nótese que en este caso no se usa =, se usa :
        numExt: 159,
        numInt: 204
    },
    tipoSangre: "O+",
    saluda (name){ // Los métodos pueden recibir parámetros y hacer uso de las propiedades del objeto
        console.log("Hola,",name,"mi nombre es ",Persona.nombre,"y vivo en",Persona.direccion.calle)
    }
} 

Persona.saluda("Lola")

// Es posible agregar propiedades y métodos a objetos ya creados

Persona.telefono = "5578990000"
console.log(Persona)

Persona.despide = (name) =>{
    console.log("Hasta luego,",name,"!")
}

Persona.despide("Lola")


// Asimismo, es posible eliminar propiedades o métodos con la palabra reservada delete

delete Persona.tipoSangre

console.log(Persona)
