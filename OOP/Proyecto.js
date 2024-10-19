
// Definición de una Base de Datos Básica

const usersDatabase = [ // Usuarios existentes
    {dbUsername: "Andres", dbPassword: "123"},
    {dbUsername: "Valeriana", dbPassword: "caracola"},
    {dbUsername: "Hyper", dbPassword:"cyan",},
    {dbUsername: "Mauricio", dbPassword:"333"},
    {dbUsername: "Caro", dbPassword:"456"},
    {dbUsername: "Lola", dbPassword:"000"},
    {dbUsername: "Heidi", dbPassword:"comet"},
    {dbUsername: "Mariana", dbPassword:"789"}
];

const usersTimeline=[ // Feed de la red social
    {username:"Estefany",timeline:"Me encata Javascript!",},
    {username:"Oscar",timeline:"yay!",},
    {username:"Mariana",timeline:"Me encanta el cafe!",},
    {username:"Andres",timeline:"Hoy no quiero trabajar",},
];

const username = "Andres" //prompt("User: ");
const password = "1235" //prompt("Password: ");
//let goahead = false

function usuarioExistente(input1, input2){
    signInGoahead = Boolean
    for(let i = 0; i < usersDatabase.length; i++){
        if((usersDatabase[i].dbUsername === input1) && (usersDatabase[i].dbPassword === input2)){
            signInGoahead = true
            break
        } else {
            signInGoahead = false 
        }
    }
    return signInGoahead 
}

function signIn(username,password){
    if(usuarioExistente(username,password) == true) {
        console.log(`Bienvenido a tu cuenta, ${username}`);// alert(`Bienvenido a tu cuenta ${username}`);
        console.log(usersTimeline); // Muestra el feed
    } else {
        console.log("Usuario o contraseña incorrectos"); // alert("Usuario o contraseña incorrectos");
    }
}

signIn(username,password);
