// Exercise 1
let sentence = ["my","favorite","color","is","blue"];
let correct_sentence = sentence.join ( " ");

console.log (correct_sentence);

// Exercise 2
let str1 = "mix";
let str2 = "pod";

let citrus = (str2.slice (0,2) + str1.slice (2) + " " + str1.slice (0,2) + str2.slice (2) ) ;
console.log (citrus);

// Exercise 3

let num1 = parseFloat (prompt("Enter a first number" , 10));
let num2 = parseFloat (prompt("Enter a second number" , 5));
let sum = num1 + num2;
alert ("The SUM is" + " " + sum );


console.log (typeof(num1));
