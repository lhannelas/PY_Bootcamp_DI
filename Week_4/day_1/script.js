function name_of_function(parameters) {
  //code
}

let a = 1;
let b = 2;

let sum = a + b;
console.log(sum);

// Normal function
function find_sum(num1, num2) {
  let sum = num1 + num2;
  console.log(sum);
}

// calling/Invoking a function
find_sum(a, b);
find_sum(2, 4);
find_sum(a, 3);

// function with a return value
function find_sum_return(num1, num2) {
  let sum = num1 + num2;
  return sum;
}

let result1 = find_sum_return(a, b);
console.log(result1);
console.log(find_sum_return(a, 5));

// Function without any parameter
function piece_of_code(){
  console.log(a);
  console.log("today is a great monday!");
}

piece_of_code();

// Custom function
// Take an array as parameter, return the first letter of each element

let input = [ "Joeri", "Ally", "Shivastav", "Kadeer","Laurent","Angkush", "Bruno"] 

function custom_function(input){
  // console.log(input);
  let output = '';
  for (let name of input.sort()) {
    output += name.charAt(0);
    
  }
  console.log(output);
}
custom_function(input);



function calculate_age(myAge){
  let mum = myAge * 2;
  let dad = mum * 1.2;
  console.log("My mum is " +mum);
  console.log("My dad is " +dad);
}

calculate_age(34);

function mum_age(myAge){
  let mum = myAge * 2
  return mum;
}

console.log(mum_age(34));

// Parameter missing
console.log(find_sum_return(10));

function find_sum_return_missing(num1, num2) {
  if(num2 === undefined){
    console.log("Error - Number missing")
    return(NaN);
  }
  let sum = num1 + num2;
  return sum;
}
find_sum_return_missing(10);

// Function with a default parameter

function find_sum_return_default(num1 =null, num2 =null) {
  let sum = NaN;
  if (num1 === null){
    console.log("No parameter passed!");
  }
  else if (num2 === null) {
    console.log("Second parameter is missing!");
  }
  else {
     sum = num1 + num2;
  }
  return sum;
}

console.log(find_sum_return_default(10, 18));

// Arrow Functions
sum_arrow_func = (num1, num2) => {
  let sum = num1 + num2;
  console.log(sum);
}
sum_arrow_func(a, b);

sum_arrow_func2 = (num1, num2) => console.log(num1 + num2);

sum_arrow_func2(a, b);

// object Methods

let students = {
  student_1: "Joeri",
  student_2: "Ally",
  student_3: "Shivastav",
  student_4: "Kadeer",
  student_5: "Laurent",
  student_6: "Angkush",
  student_7: "Bruno",
  exercise: function() {
    console.log(`${this.student_1} has forgot to do his homework.`);
  }

}

students.exercise();

let rectangle = {
  width: 100,
  height: 100,
  area: function(){
    return this.width * this.height
  }
}
console.log(rectangle.area());