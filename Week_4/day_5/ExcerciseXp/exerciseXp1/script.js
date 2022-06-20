let div = document.getElementById("container");
console.log(div);

console.log(document.querySelectorAll('li')[0]);

let elem_txt = document.querySelectorAll('li')[1];
elem_txt.textContent = "Richard";


let name1 = document.querySelectorAll('li')[0];
name1.textContent = "Laurent";

let name2 = document.querySelectorAll('li')[2];
name2.textContent = "Laurent";

console.log(document.querySelectorAll('ul'));


let parentelem = document.querySelectorAll('ul')[1];
let childelem = document.querySelectorAll('li')[3];
parentelem.removeChild(childelem);

console.log(document.querySelectorAll('ul')[1]);

let newC = document.querySelectorAll('ul')[0];
console.log(newC.getAttribute('class'));
newC.classList.add('Student_list', 'university', 'attendance');

let newC1 = document.querySelectorAll('ul')[1];
newC1.classList.add('Student_list');