console.log("Intro to DOM");

//let elem = document.getElementById('title');
//console.log(elem);
//
//elem.style.color = 'red';
//elem.innerText = 'Welcome to DOM!';
//elem.style.backgroundColor = 'blue';

let body = document.body
console.log(body);

// Accessing DOM elements
console.log(body.firstChild); // first node
console.log(body.firstElementChild.textContent); // first Element
// childNodes returns nodes: Element nodes, text nodes, and comment nodes.
// Whitespace bet elements are also text nodes.
console.log(body.childNodes); // retrieve all nodes
console.log(body.children); // retrieve elements only
console.log(body.children[0]); 
console.log(body.childNodes[1]);

// retrieve div1-p1
console.log(body.children[1].firstElementChild);

//using id
let div1p1 = document.getElementById('div1p1');
console.log(div1p1);

// using tag
let divs = document.getElementsByTagName('div');
//console.log(divs[0]);
for (let div of divs) {
  console.log(div);
}

//using class
let reds = document.getElementsByClassName('red');
for (let red of reds) {
  console.log(red);
}

//Query Selector
let h1 = document.querySelector('h1');
console.log(h1);  

let div_query = document.querySelectorAll('h1 +div'); //'h1+div' , 'h1~div', 'div', 'div p', 'div> p'
for (let div of div_query) {
  console.log(div);
}



// Exercise1 (John and Peter)
// Get div
console.log(document.body.firstElementChild);
console.log(document.body.children[0]);
console.log(document.getElementsByTagName('div')[0]);
console.log(document.querySelector('div'));
console.log(document.querySelectorAll('div')[0]);

//ul
console.log(document.body.firstElementChild.nextElementSibling);
console.log(document.body.children[1]);
console.log((document.getElementsByTagName('ul')[0]));
console.log(document.querySelectorAll('ul'));
console.log(document.querySelectorAll('ul')[0]);

// 2nd li
console.log(document.body.children[1].lastElementChild);
console.log(document.getElementsByTagName('li')[1]);
console.log(document.querySelectorAll('li')[1]);

// Create Element
let elem_h2 = document.createElement('h2');
elem_h2.textContent = "It is very cold at night lately.";
console.log(elem_h2);
// div1p1.appendChild(elem_h2);
body.appendChild(elem_h2);

for (let i=0; i<5; i++) {

let new_div = document.createElement("div");
new_div.style.height = '100px';
new_div.style.width = '100px';
new_div.style.border = '1px solid black';
new_div.style.borderRadius = '5px';
new_div.style.margin = '5px';
new_div.style.backgroundColor = 'yellow';
body.appendChild(new_div);

}

//innerText and innerHTML
let elem_txt = document.querySelector('#div2');
console.log(elem_txt);
elem_txt.textContent = 'Hi!';
//careful whem using these 2. They override whatever is in the tag
// elem_txt.innerText = '<h3>Hi!</h3>';
// elem_txt.innerHTML= "<h3>Hi!</h3>";

// Attributes
console.log(elem_txt.hasAttribute('id'));
console.log(elem_txt.getAttribute('id'));
elem_txt.setAttribute('id', 'div2-2');
console.log(elem_txt.id);
elem_txt.id = 'laurent'

elem_txt.setAttribute('username', 'admin');
elem_txt.removeAttribute('id');

// style
elem_txt.style.color = 'blue';
elem_txt.style.backgroundColor = 'yellow';

//
elem_txt.setAttribute('class', 'class_1' );
elem_txt.setAttribute('class', 'class_2 class_3 ' );
console.log(elem_txt.className);
elem_txt.className = 'class_0';
elem_txt.classList.add('class_4');