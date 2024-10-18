
// Desde 2015, JS adoptó una nueva forma de instanciar objetos a a través de una clase

class Persona{
    constructor(parametro1, parametro2, parametro3){
        this.nombre = parametro1
        this.apellido = parametro2
        this.edad = parametro3
    }
    saludar(input){
        console.log("Hola,",input,"mi nombre es",this.nombre)
    }
}

Heidi = new Persona("Heidi","Galicia",10)
Heidi.saludar("Lola")
