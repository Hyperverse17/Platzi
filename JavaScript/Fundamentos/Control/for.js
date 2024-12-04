
/* Estructura básica

for (variable; condición; incremento){
     Código
}*/

let actionList = ["eat", "sleep", "coffee", "code", "coffee", "repeat"] // para esta lista lenght es igual a 6, sin embargo, al gual que en Python, los elementos se empiezan a contar desde 0
numberOfElements = actionList.length

for (let iterator = 0; iterator < numberOfElements; iterator++){ // Como los elementos se empiezan a contar desde cero, la condición debe estar dada por "<", no por "<="
    console.log(`Action ${iterator} - ${actionList[iterator]}`)
}

// Ciclo for ...of
// Es una forma de iterar sobre los elementos de un string o de un array. Con esta modalidad del for se ahorran muchas líneas de código
// Este ciclo funciona sobre elementos iterables


// Ejemplo con arrays
let canasta = ["Huevo","Leche","Azúcar","Manzanas","Café"]

for (producto of canasta){
    console.log(`La canasta contiene: ${producto}`);
}

// Ejemplo con strings

let alphabet = "abcdefghijklmnropqrstuvwxyz"
let counter = 0
for (letter of alphabet){
    counter += 1
    console.log(`Letter ${counter}: "${letter}"`)
}

// Ciclo for ..in
// Es similar a for ... of, sin embargo, este se usa para iterar sobre elementos NO iterables como objetos
// for ...of --> itera sobre strings y arrays
// for ...in --> itera sobre objetos

// Ejemplo de uso de for ...in

const listaDeComparas = { // Const, a diferencia de un array o de un string, es un objeto NO iterable
// Las variables declaradas con const mantienen valores constantes. Las declaraciones const similitudes con las declaraciones let.
    manzanas: 7,
    peras: 5,
    naranjas: 3,
    bananos: 0, 
};
// la sentencia console.log(listaDeComparas) devuelve algo así: { manzanas: 7, peras: 5, naranjas: 3, bananos: 0 }

for (elemento in listaDeComparas){
    console.log(elemento); // De esta forma se accede al "nombre" del elemento, no al valor del mismo
};

// para imprimir cada elemento con su respectivo valor:

for (elemento in listaDeComparas){
    console.log(`Comprar: ${listaDeComparas[elemento]} ${elemento}`) // el primer parámetro hace referencia al valor del elemento, el segundo hace referencia al nombre del elemento
}

