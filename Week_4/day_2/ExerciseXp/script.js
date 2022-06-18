// Exercise 1

function infoAboutme() {
  console.log("I am Laurent, 34 years old and I play poker")
}

infoAboutme();


function infoAboutPerson(personName, personAge, personFavoriteColor) {
  console.log("Your name is " + personName + "," + " your age is " + personAge + " and your favorite color is " + personFavoriteColor)
}

infoAboutPerson("David", 45, "blue"); 
infoAboutPerson("Josh", 12, "yellow"); 

// Exercise 2

function calculateTip() {
  // let billAmount = parseFloat(prompt("What is the bill amount?"));
  let tip = " "

  if (billAmount < 50) {
    tip = 0.2 * billAmount
  }
  else if (billAmount >= 50 && billAmount <= 200) {
    tip = 0.15 * billAmount
  }
  else {
    tip = 0.1 * billAmount
  }

  console.log (billAmount + tip);

}

// calculateTip();

// Exercise 3

function isDivisible(divisor) {
  
  let sum = 0;
  
  for (let i = 0; i < 501; i += divisor) {
    console.log (i);
    sum += i;
  }
   console.log(sum);
}

isDivisible(23);
isDivisible(3);
isDivisible(45);

// Exercise 4

let stock = { 
  "banana": 6, 
  "apple": 0,
  "pear": 12,
  "orange": 32,
  "blueberry":1
}  

let prices = {    
  "banana": 4, 
  "apple": 2, 
  "pear": 1,
  "orange": 1.5,
  "blueberry":10
} 

let shoppingList = ["banana", "orange", "apple"];

function myBill() {
  let total = 0;
  // Loop through shopping list
  for (let item of shoppingList) {
    // Check if item is in stock
    if (stock[item] > 0){
      // Add price to total
      total += prices[item];
      // Update stock
      stock[item]--;
    }
  }
  console.log(stock);
  return total
} 

console.log(myBill());

// Exercise 5

function changeEnough(itemPrice, amountOfChange) {
  let sum = 0;

  for (let i = 0; i <amountOfChange.length; i++) {
    sum += i
  }
}

// Exercise 6

function hotelCost() {
  let num_nights = null;
   

  do {
    num_nights = prompt("How many nights would you like to stay in the hotel?"); 
    num_nights = Number(num_nights);

  }

  while ( isNaN(num_nights) || num_nights <= 0) 
     
    return num_nights * 140
  }

  console.log(hotelCost());

