//Exercise 1

let people = ["Greg", "Mary", "Devon", "James"];

people.shift();
console.log(people);

people.splice(2, 1, "Jason");
console.log(people);

people[3] = "Laurent";
console.log(people);

console.log(people.indexOf("Mary"));

console.log(people.slice(1));

console.log(people.indexOf("Foo")); // It returns -1 meaning not found because Foo is not in the array.

let last = people[people.length - 1];
console.log(last);

for ( let names in people ) {
  
  console.log(people[names]);

  if (people[names] === "Jason") {
    break;
  }
}

//Exercise 2
let colors = ["black", "white", "red", "green", "yellow"];

for (let favorite in colors) {
  
  console.log("My #" + (parseFloat(favorite)+1) + " choice is " + colors[favorite]);
}



//Exercise 3 
let number = 0;

do {
  number = parseFloat(prompt("Please enter a number"));
  number++;
}

while (number < 10);


// Exercise 4

let building = {
  numberOfFloors : 4,
  numberOfAptByFloor : {
      firstFloor : 3,
      secondFloor : 4,
      thirdFloor : 9,
      fourthFloor : 2,
  },
  nameOfTenants : ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent:  {
      sarah: [3, 990],
      dan :  [4, 1000],
      david : [1, 500],
  },
}

console.log(building.numberOfFloors);

console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);

console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0]);

let sumOfRent = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1];
console.log(sumOfRent);

if (sumOfRent > building.numberOfRoomsAndRent.dan[1]) {
  building.numberOfRoomsAndRent.dan.splice(1, 1, 1200);
} 

console.log (building);


//Exercise 5

let family = {
  father : "Lloyd",
  mother : "Gillian",
  brother : "Olivier",
  sister : "Amelia",
  wife : "Elodie",
}

console.log (family);

for ( let key in family){
  console.log (key);
  console.log (family[key]);
}

//Exercise 6

let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

for ( let phrase in details ){
  // let str = details.
  // let str = String(phrase);
  // let str1 = String(details[phrase]);
  console.log (phrase);
  console.log (details[phrase]);
  
  
}

//Exercise 7
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
console.log (names);

let secret = '';
for ( let secret in names){
  console.log (names[secret][0]);
}

