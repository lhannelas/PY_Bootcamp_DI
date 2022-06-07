console.log ("This is from the JS script");

// Declare a variable
let a = 5;
let b = 3;
let first_name = "Damien"; // snake_case style
let firstName = "Damien"; // camelCase style

console.log(a);
console.log(b);
console.log(a + b);
console.log(a - b);

let sum = a + b;
console.log(sum);

// Update the vakue of the variable
a = 2;
console.log(a);
console.log(b);
console.log(sum);

sum = a + b;
console.log(sum);

b=  4;
console.log(sum);

sum = a + b;
console.log(sum);

// Primitive Data Types
// Numbers - digits 0-9
// Strings - "" or '' or ``
// Booleans - True or False (1 or 0)
// Undefined - no value assigned
// null - special value that does not belong to any of the above

// undefined
let c;
console.log(c);

// null
let d = null;
console.log(d);

// string
let str = "This is a  great day";
console.log(str);

let str1 = "hello"
let str2 = " world"

// concatenation
console.log(str1 + " " + str2);

console.log(`${str1} ${str2}`);

let str3 = "1";
let str4 = "3";
let str5 = "5";

console.log (str3 + str4);
console.log (str3 - str4);

console.log (str3 + str5);
console.log (str3 - str5);

// Convert a string to a number
console.log(str3); //string
str3 = Number(str3); //number
console.log(str3);

console.log(str4); //string
str4 = Number(str4); //number
console.log(str4);

console.log(str3 + str4);


// string methods - in-built functions to manipulate the type
// let str1 = "Hello";

console.log(str1.length); // length property
console.log(str1.indexOf('o')); //index starts from zero
console.log(str1.indexOf('l')); // returns the first match
console.log(str1.indexOf('w')); // returns -1 means no match

console.log(str1.substring(1, 4)); // return character from start index up to but not including value at end index
console.log(str1.substring(1)); // from start index till end of string

console.log(str1.substring(
	str1.indexOf('e'), // 1
	str1.indexOf('o') + 1 // 4+1
	));

console.log(str1.toLowerCase());
console.log(str1.toUpperCase());
console.log(str1.concat(str2));
// remove blank space
console.log(str2);
console.log(str2.trim());
console.log(str2.trimStart());
console.log(str2.trimEnd());

// Number Methods
let num1 = 4; //positive
let num2 = -3; //negative
let num3 = 10000000000
let pi = 3.14159265358979238; // decimal (float)

// can do arithmetic operations: + - * /
// Convert to string

console.log(num1);
console.log(num1.toString());
/*console.log(num3.toLocalString());*/

// Decimal places
console.log(pi.toFixed(3)); // became a string in the processµ
console.log(pi.toFixed(0)); // no decimal places

// Check if a variable is not a Number
console.log(isNaN(pi));
console.log(isNaN("number"));

// Boolean - True (1) or False (0)
let status = true;

console.log(status);
console.log(Number(status));

let expression = Boolean (10 < 9);
console.log(expression);

// Comparisons
/*
= means assign
== means compare value only
=== means compare value and data
*/

let var1 = 5
let var2 = "5"

console.log(Boolean ( var1 == var2));
console.log(Boolean ( var1 === var2));
console.log(Boolean ( var1 != var2));
console.log(Boolean ( var1 !== var2));

/*
! - NOT
|| - OR
&& - AND
*/

// OR : At least one has to be true for the expression to be true
console.log(Boolean((var1 < 10) || (var1 === var2)));
// AND: All conditions have to be true for the expression to be true
console.log(Boolean((var1 > 10) && (var1 === var2)));

// User Inteface Functions
// Alert
alert("wake up")

// Prompt - ask user for an input
let input = prompt("Please enter your name")
console.log(input);

let num = prompt( "Please enter a number:");
num = Number(num);
console.log(num);

// Confirm - Ask a question (true or false)
let isOk = confirm ("Are your confused with Javascript?");
console.log(isOk);

