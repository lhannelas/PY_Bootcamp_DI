console.log("conditionals")

let a = 'l';

// Only the IF statement
console.log("Before if statement");
if (a > 0){
	//execute your code
	console.log("a is greater than zero");
}
console.log("After if statement");

// If and else statement
console.log("Before if else statement");
if (a > 0){
	//execute your code if expression is true
	console.log("a is greater than ten");
}
else{
	//execute code if expression is false
	console.log("a is not greater than ten");
}
console.log("After if else statement");

// If.. Else If...Else statement

console.log("Before If.. Else If...Else statement");
if (a > 0){
	//execute your code if expression is true
	console.log("a is greater than zero");
}
else if (a < 0){
	console.log("a is smaller than zero");
}
else if (a === 0){
	console.log("a is equal to zero");
}
/*else{*/
	//execute code if expression is false
/*	console.log("an unexpected error happened");
	if (isNan(a)){
		console.log("'a' is not a number. Please check the data type.")
	}

console.log("After If.. Else If...Else statement");*/

//Exercise 1

let age = prompt ("How old are you?");

if (age < 18){
	alert("Sorry, you are too young to drive this car. Powering off");
}
else if (age == 18){
	alert("Congratulations on your first year of driving. Enjoy the ride!");
}
else if (age > 18){
	alert("Powering On. Enjoy the ride!");
}
else if (isNaN(age)){
		alert("'age' is not a number. Please check the data type.")
}

// switch case
let c = 1;

switch (c) {
	case 0:
		console.log(0);
		break;
	case 1:
		console.log(1);
		break;
	case 2:
		console.log(2);
		break;

}


let browser = "pokemon";

if (browser === "Edge") {
	alert ("you've got the Edge!");
	}
else if (browser === "Chrome" ||
				 browser === "Firefox" || 
				 browser === "Safari" || 
				 browser === "Opera") {
	alert ("We support these browers too");
}
else {
	alert ("We hope this page looks ok!");
}
