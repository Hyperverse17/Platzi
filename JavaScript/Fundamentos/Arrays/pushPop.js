
// Métodos que modifican el array (Mutability)
// push añade uno o más elementos al final del array 

const countries = ["mexico", "Canada", "Alemania", "Suiza"]
const toAddCountries = countries.push("Suecia", "Noruega", "Finlandia") // push devuelve también la nueva longitud del array

console.log(countries) // Devuelve la modificacion del array original

console.log(toAddCountries) // devuelve la nueva longitud del array modificado

// pop elimina el último elemento del array y devuelve el elemento eliminado

const removedCountry = countries.pop()

console.log(countries)
console.log(removedCountry)
