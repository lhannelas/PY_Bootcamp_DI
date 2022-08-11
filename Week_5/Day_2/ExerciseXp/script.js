//Exercise 1
//1
console.log(document.querySelector("h1"));

//2
console.log(document.querySelector("article"));
console.log(document.querySelectorAll("p")[3]);

let parentelem = document.querySelector("article");

let childelem = document.querySelectorAll("p")[3];

parentelem.removeChild(childelem);

//3
let clickred = document.getElementById("clickred");
console.log(clickred);

clickred.addEventListener("click", function(ev){
  clickred.style.backgroundColor = 'red'; 
  ev.stopPropagation();
});

//4
let hide = document.getElementById("hide");
console.log(hide);

hide.addEventListener("click", function(ev){
  hide.style.display = 'none';
});

//5
console.log(document.querySelectorAll("p")[0]);
let p1 = document.querySelectorAll("p")[0];
let p2 = document.querySelectorAll("p")[1];
let p3 = document.querySelectorAll("p")[2];

function bold(){
  p1.style.fontWeight = "bold";
  p2.style.fontWeight = "bold";
  p3.style.fontWeight = "bold";
  console.log("go bold");
}

//6
let font = document.getElementById("font");
console.log(font);

font.addEventListener("mouseover", function(ev){
  font.style.fontSize= Math.floor(Math.random() *101) + 'px';
});


// Exercise2
