
class Animal {
    constructor(nombre, tipo) {
      this.nombre = nombre;
      this.tipo = tipo;
    }
    emitirSonido() {
      console.log("El",this.tipo,"emite un sonido");
    }
  }
  
  const gato1 = new Animal("Garfield","Gato")
  gato1.emitirSonido()

  const ave1 = new Animal("Beto","Perico")

  class Perro extends Animal {
    constructor(nombre, tipo, raza) {
      super(nombre, tipo); // con super se indican las propiedades heredadas de la super clase
      this.raza = raza;  // Esta propiedad seria la nueva para esta clase
    }
    emitirSonido() {  // Se puede redefinir un método existente en la super clase
        console.log(this.nombre,"ladra");
    }
    correr() {
      console.log(`${this.nombre} corre alegremente`);
    }
  }
  
  const perro1 = new Perro("Lola", "Perro", "Maltes");
  const perro2 = new Perro("Heidi", "Perro", "Maltes")
  
  console.log(perro1);
  perro1.correr();
  perro1.emitirSonido();

  perro1.nuevoMetodo = function() {
    console.log("Este es un nuevo metodo solo para",this.nombre);
 };

 perro1.nuevoMetodo()
 // perro2,nuevoMetodo() // Responde: perro2,nuevoMetodo() ReferenceError: nuevoMetodo is not defined

 Perro.prototype.segundoMetodo = function() {
    console.log("Este es un nuevo metodo para",this.nombre,"y todos los",this.tipo);
 };
 
perro1.segundoMetodo()
perro2.segundoMetodo()

 Animal.prototype.tercerMetodo = function() {
    console.log("Este es un metodo para",this.nombre,"y todos los",this.tipo);
 };

 ave1.tercerMetodo()
 perro2.tercerMetodo()
 gato1.tercerMetodo()
 perro1.tercerMetodo()

