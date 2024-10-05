
let producto = "Guitarra"

switch (producto){ // Variable sobre la que se aplicará el switch
    case "A":
        console.log("Elegiste el producto A");
        break; // Siempre debe terminar con break

    case "B":
        console.log("Elegiste el producto B");
        break;

    case "C":
        console.log("Elegiste el producto C");
        break;

    default:
        console.log(`No existe "${producto}"`); //Las comillas invertidas permiten concatenar variables en strings
}
