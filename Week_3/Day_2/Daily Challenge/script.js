//Exercise 1 
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift ();

console.log (fruits);

fruits.sort ();

console.log (fruits);

fruits.push ("Kiwi");

console.log (fruits);

fruits.splice (0,1);

console.log (fruits);

fruits.reverse ();

console.log (fruits);

//Exercise 2
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log (moreFruits[1][1]);