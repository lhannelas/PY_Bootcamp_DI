console.log("xp2");

let body = document.body;
console.log(body.firstElementChild);
let div = body.firstElementChild;

div.style.backgroundColor = "lightblue";
div.style.padding = "10px";

console.log(document.querySelector('li'));
 let john = document.querySelector('li');

 john.style.visibility = "hidden";

 let pete = document.querySelectorAll('li')[1];
 pete.style.border = "1px solid red";

 body.style.fontSize = "20px";

 if (div.style.backgroundColor === 'lightblue') {
  alert("Hello John and Pete");
 }