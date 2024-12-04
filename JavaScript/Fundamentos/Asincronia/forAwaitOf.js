
// Existe una forma de procesar distintas promesas con async y await mediante un loop especial
// El loop es For Await y es una modificación del for tradicional

// Creación del arreglo sobre el cual se va a iterar

let url1 = "https://rickandmortyapi.com/api/character"
let url2 = "https://rickandmortyapi.com/api/location"
let url3 = "https://rickandmortyapi.com/api/episode"
let url4 = "https://pokeapi.co/api/v2/pokemon/ditto"
let url5 = "https://gateway.marvel.com:443/v1/public/characters?apikey="

const urlArray = [url1,url2,url3,url4,url5];

async function fetchLoop() {
    try{
        for await (let urli of urlArray){
            let responsei = await fetch(urli);
            let datai = await responsei.json();
            console.log(datai);
        }
    } catch(error){
        console.log(error)
    }
}

fetchLoop()
