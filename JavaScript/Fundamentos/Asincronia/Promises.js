
const promiseExample = new Promise((resolve, reject) => { // el consructor Promise recibe dos funciones como parámetros
    setTimeout (() => { // Se crea una función de timeout para controlar el flujo
        let successFlag = true;
        if (successFlag){
            resolve("Operación Exitosa! 🚀"); // La función resolve se ejecuta cuando la promesa se resuelve
        } else {
            reject("Operación Fallida 💀"); // La función reject se ejecuta cuando la promesa NO se resuelve
        }
    },1000); // Se da un tiempo de 1000 ms para resolver esta tarea
});

console.log(promiseExample)

promiseExample
    .then((successMessage) => { // maneja el caso de de exito
        console.log(successMessage);
    });

promiseExample
    .catch((errorMessage) => { // // maneja el caso de de error
        console.log(errorMessage);
    });


promiseExample
    .finally(() => { // Se ejecuta al final independientemente del exito o fracaso
        let whatToDo = "Que hacemos ahora?";
        console.log(whatToDo);
    })

    console.log(promiseExample)
    
    
