
// Simulacion de obtencion de datos en un servidor usando promesas

function getServerData(id){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id == 1707){
                resolve({
                    id: 1707,
                    nombre: "Otelo",
                    apellido: "Galicia",
                    edad: 33
                    }); // La función resolve se ejecuta cuando la promesa se resuelve
            } else {
                reject("Usuario No encontrado 💀"); // La función reject se ejecuta cuando la promesa NO se resuelve
            }
        },1000);
    });
};

// Uso de la promesa

console.log("...Iniciando Búsqueda")

getServerData(1707) // Nótese el uso de dos .then() en serie
  .then((usuario) => {
    console.log("Usuario encontrado:", usuario)
    return usuario.edad // Esta funcion regresa la edad
  })
  .then((edad) => { // Este nuevo then toma como argumento el return del anterior
    console.log("La edad del usuario es:", edad)
  })

  .catch((error) => {
    console.error(error) // nueva función!
  })

  .finally(() => {
    console.log("Busqueda finalizada")
  })