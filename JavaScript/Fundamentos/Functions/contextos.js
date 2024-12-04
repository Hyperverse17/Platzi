
// Contexto global > Desde aquí no se puede acceder a elementos de contextos locales
const productName = "Smartphone"
const price = 499
const brand = "GlobApple"

function getProductDetails(){
    // Contexto local > Desde aquí sí se puede acceder a elementos del contexto global
    const productName = "Laptop"
    const price = 899
    return `The ${productName} ${brand} costs: $${price}` // Uso de variables locales y una global
}

console.log(getProductDetails())
console.log(`The ${productName} ${brand} costs: $${price}`) // Uso de variables globales
