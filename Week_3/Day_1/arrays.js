console.log("arrays");

// array - List of values
let students = [ "Angkush", "Joeri", "Laurent", "Shivastav", "Kadeer", "Ally", "Bruno"]
console.log(students);

// Get an element from an array
console.log(students[0]);
console.log(students[1]);
console.log(students[2]);
console.log(students[3]);
console.log(students[4]);
console.log(students[5]);
console.log(students[6]);

// Get the number of elements inside an array
console.log(students.length);

// update and element in an array
// Joeri to Yuri
students[1] = 'Yuri' ;
console.log(students[1]);

// Add a new element inside an array
// ( at the last position)
students[7] = "Damien"; 
students[students.length] = "yeshna";
console.log (students);

// Nested Arrays
let student_array = [
 ["Angkush",19],
 ["Joeri", 35 ],
 ["Laurent", 34, ["olivier","Amelia"] ]
 ["Shivastav", 24 ],
 ["Kadeer", 24 ],
 ["Ally", 33 ], 
 ["Bruno", 55],
]

console.log(student_array[2][1]);