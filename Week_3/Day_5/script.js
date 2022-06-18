// Loops
let arr = ['a', 'b', 'c', 'd'];

console.log(arr[0]);
console.log(arr[1]);
console.log(arr[2]);
console.log(arr[3]);

// For loops

// starting condition (e.g. i = 0)
// condition to be evaluated ( loop until the condition is not longer true)
// increment (e.g. i += 1, i++)

for (let i = 0; i < 10 ; i++) {
  console.log(i);
}

for (let i = 0; i < arr.length; i++ ) {
  console.log(arr[i]);
}

// For in loop - Arrays and Objects
for (let i in arr){
  console.log(i, arr[i]);
}

let obj = {
  user: "damien",
  email: "damien@developers.institute",
  phone: 5509123
}

for (let key in obj){
  console.log(key, obj[key]);
}

// for of - only for array and string
for(let val of arr){
  console.log(val);
}

// ForEach - array method
arr.forEach(i => console.log(i));


// while
// while (condition){
//   // statements
// }

let count = 0;

while (count < arr.length){
  console.log(arr[count]);
  if(arr[count] === 'c') {
    break;
  }
  count++;
}

// Infinite loops - while(1) or while(true)

// let val = 0;
// while(val < 10){
//   console.log(val);
// }

for (let i in arr){
  if (arr[i] === 'c') {
    continue;
  }
console.log(i, arr[i]);
}


// DO - while loop
// codes will be executed at least once

let day = 0;
do {
  console.log("Today is a great evening");
  day++
}
while (day > 5)

// check passord example
// let pw = '';
// let pw_len = pw.length;

// do {
//   pw = prompt ("Please enter the password with at least 8 characters:");
//   pw_len = pw.length;
// } while (pw_len < 8);

// console.log("thank you");

// Exercise 1

let array = [ 0 , 1 , 2 ,3 ,4, 5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15];

for (let i = 0; i <=15 ; i++ ) {
  let remainder = i % 2;
  if ( remainder === 0) {
    console.log(i + " is even");
      }
  else {
  console.log(i + " is odd");
}
}

// Exercise 2

let names = ["john", "sarah", 23, "Rudolf", 34];

for (let name of names) {
  let name_type = typeof name;

  if ( name_type === "string") {
    name = name.replace(name.charAt(0), name.charAt(0).toUpperCase());
    console.log(name);
  }
 
}

// while (i < names.length) {
//   character = names.charAt(0);
//   if (character == character.toLowerCase()) {
//     console.log(names.charAt(0).toLowerCase() + names.slice(1));
//   }
// }


