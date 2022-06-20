console.log("XP3");
let body = document.body;

let div = document.body.firstElementChild;
console.log(div);
div.setAttribute("id", "socialNetworkNavigation");


let newElement = document.createElement("li");
newElement.textContent = "Logout";

let ul = document.querySelector("ul");
ul.appendChild(newElement);

console.log(ul.firstElementChild.textContent);
console.log(ul.lastElementChild.textContent);




