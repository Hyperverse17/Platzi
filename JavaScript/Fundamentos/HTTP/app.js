
fetch("https://jsonplaceholder.typicode.com/posts") // fetch siempre va a ser un get por defecto
  .then((response) => response.json())
  .then((data) => console.log(data));
