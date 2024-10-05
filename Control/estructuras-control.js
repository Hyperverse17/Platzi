
// Estructura de control if

let nombre = prompt("Nombre ","") // Se usa para abrir una ventana de ingreso de datos (solo en consola de chrome)

//numeroJugador=parseInt(prompt("Adivina el numero secreto entre el 1 al 10"));

if (nombre == "Valeria"){ // La condición deseada se coloca entre paréntesis
    // El bloque de código se coloca dentro de las llaves
    console.log("Bienvenida, Valeria")

} else if (nombre == "Otelo") { // Else if es opcional. Se pueden anidar tantos como se desee a modo de switch case
    console.log("Bienvenido, Otelo")

} else if (nombre == "Jovani") {
    console.log("Bienvenido, Jovani")

} else { // else es opcional, es la contraparte del if
    console.log("Usuario no encontrado")
}
