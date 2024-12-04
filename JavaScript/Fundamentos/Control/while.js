
/*
while (condicion){
    código
}
*/

// Ejemplo while --> Primero se evalúa la condición antes de ejecutar el código
let contador1 = 1;
while (contador1 <= 10){
    console.log(`Ciclo while: ${contador1}`);
    contador1++;
}

// ejemplo do while --> Primero se ejecuta el código antes de evaluar la condición

let contador2 = 1;
do{
    console.log(`Ciclo do-while: ${contador2}`);
    contador2++;
} while (contador2 <= 10)
