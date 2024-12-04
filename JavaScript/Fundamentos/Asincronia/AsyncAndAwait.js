
// 1. Ejemplo de fetch sin Async ni Await
function fetchRickAndMorty(){  // Se crea una función que hará fetch a una api pública
    fetch("https://rickandmortyapi.com/api/character") // Como esta, existen muchas apis públicas
    .then((response) => response.json()) // Con el método .then se procesa la respuesta exitosa, el método .json convierte esta respuesta a este formato
    .then((data) => console.log(data))
    .catch((error) => console.log(error)); // Con el método .catch se procesa el error
};

//fetchRickAndMorty()

// 2. Ejemplo de fetch con uso de Async y Await
async function fetchRickAndMortyAsync() {
    try{ // la cláusula try se usa de la mano con funciones async. Dentro de esta se coloca lo que debería suceder
        let fetchResponse = await fetch("https://rickandmortyapi.com/api/character"); // Anteponiendo await, estamos indicando que se debe esperar la respuesta antes de continuar
        let data = await fetchResponse.json();
        console.log(data)
    } catch(error){  // la cláusula catch es la contraparte de try, aquí se procesan errores
        console.log(error)
    }
}

fetchRickAndMortyAsync()
