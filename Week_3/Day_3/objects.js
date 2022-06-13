
// Declare an object
let obj = {};

let students = {
  student_1: "Joeri",
  student_2: "Ally",
  student_3: "Shivastav",
  student_4: "Kadeer",
  student_5: "Laurent",
  student_6: "Angkush",
  student_7: "Bruno"
}

console.log(students);

// Access value of a key inside an object
console.log(students.student_1);
console.log(students["student_1"]);

let a = "student_2";
console.log(students[a]);

let database = {
  student_1: {
    name: "Joeri",
    surname: "Smissaert",
    age: 35
  } ,
  student_2: {
    name: "Ally",
    surname: "Baubooa",
    age: 24
  } ,
  student_3:{
    name: "Shivastav",
    surname: "Jugoo",
    age: 24
  } ,
  student_5: {
    name:"Laurent",
    surname:"Hannelas",
    age: 34
  },
  student_7: {
    name:"Bruno",
    surname:"Beche",
    age: 50
}
}

console.log(database.student_2.age);

// Add/change object properties
database.student_2.age = 21;
console.log(database);

database.student_2.laptop = "Asus Vivobook";
console.log(database);

// Deleteobject property
delete database.student_2.laptop;
console.log(database);


let code = {
  
    username: "lhannelas",
    password: "britney10"
 
  }
  


console.log(code);

let database_2 = [code];
console.log(database_2);

// or let database_2 = [
//   {
//     username: "lhannelas",
//     password: "britney10"
//   }
// ]



let newsfeed = [

  {
    username: "lhannelas",
    timeline: "timeline1"
  },
  {
    username: "polico",
    timeline: "timeline2"
  },
  {
    username: "Ton",
    timeline: "timeline3"
  }
]

console.log(newsfeed);