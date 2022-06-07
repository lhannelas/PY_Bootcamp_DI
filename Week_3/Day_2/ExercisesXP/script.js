//Exercise 1
let fav_food = "pizza";
let fav_meal = "lunch";

console.log("I eat" + " " + fav_food + " " + "at every" + " " + fav_meal);

//Excercise 2
//Part I
//1.
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;

console.log (myWatchedSeriesLength);

//2.
let myWatchedSeriesSentence = "Casa de Papel, Queen of the South, and Mr Robot"

//3.
console.log ("I watched" + " " + myWatchedSeriesLength + " series :" + " " + myWatchedSeriesSentence );

//Part II
//1.
myWatchedSeries[2] = "friends";

//2.
myWatchedSeries.push ("Casa de Papel"); //or could have used myWatchedSeries[3] = "Casa de Papel"

//3.
myWatchedSeries.unshift ("Mr Robot");

//4.
myWatchedSeries.splice (1,1);

//5.
console.log (myWatchedSeries[1][2]);

//6.
console.log (myWatchedSeries);

//Exercise 3
//1.
let celsius = 15

//2.
let fahrenheit = (celsius / 5 * 9 + 32);
console.log (celsius + "°C is" + " " + fahrenheit + "°F.");

//Exercise 4
let c;
let a = 34;
let b = 21;

console.log(a+b); //first expression
//1. Prediction: 55 , because a and b are numbers so 34 + 21
// Actual: 55

a = 2;

console.log(a+b) //second expression
//2. Prediction: 23 , because the value of a has been replaced by 2 and b is the same number so 2 + 21
// Actual: 23

//3. The value of c is undfined

console.log(3 + 4 + '5');
//4. Prediction: 75 , because 3 and 4 are numbers and 5 is a string
// Actual : 75

//Exercise 5
console.log (typeof(15));
// Prediction: number
// Actual: number

console.log (typeof(5.5));
// Prediction: number
// Actual: number

console.log (typeof(NaN));
// Prediction: number
// Actual: number

console.log (typeof("hello"));
// Prediction: string
// Actual: string

console.log (typeof(true));
// Prediction: boolean
// Actual:

console.log (typeof(1 != 2));
// Prediction: boolean
// Actual: boolean

console.log (typeof("hamburger" + "s"));
// Prediction: string
// Actual: string

console.log (typeof("hamburgers" - "s"));
// Prediction: number
// Actual: number

console.log (typeof("1" + "3"));
// Prediction: string
// Actual: string

console.log (typeof("1" - "3"));
// Prediction: number
// Actual: number

console.log (typeof("johnny" + 5));
// Prediction: string
// Actual: string

console.log (typeof("johnny" - 5));
// Prediction: number
// Actual: number

console.log (typeof(99 * "hello"));
// Prediction: number
// Actual: number

console.log (typeof(1 != 1));
// Prediction: boolean
// Actual: boolean

console.log (typeof(1 == "1"));
// Prediction: boolean
// Actual: boolean

console.log (typeof(1 === "1"));
// Prediction: boolean
// Actual: boolean

//Exercise 6
console.log (5 + "34");
// Prediction: 534 ,because 5 is a number, 34 a string and the + will concatenate the data
// Actual: 534

console.log (5 - "4");
// Prediction: 1 ,because even is 5 is a number and 4 is a string, the - sign will make javascript try to convert 4 into a number to do the equation
// Actual: 1

console.log (10 % 5);
// Prediction: 0 ,because there is no remainder when 10 is divided by 5
// Actual: 0

console.log (5 % 10);
// Prediction: 5, because the remainder is 5
// Actual: 5

console.log ("Java" + "Script");
// Prediction: JavaScript , because it is 2 string concatenate 
// Actual: JavaScript

console.log (" " + " ");
// Prediction: empty spaces because two empty spaces which are strings have been concatenate
// Actual: empty spaces

console.log (" " + 0);
// Prediction: 0, because the first item is an empty string and the other item a number 
// Actual: 0

console.log (true + true);
// Prediction: true, because both item are boolean and when all item is true the outcome is true
// Actual: 2 

console.log (true + false);
// Prediction: 1 , because I learned from my mistake and the value of true is 1 and false is 0
// Actual: 1

console.log (false + true);
// Prediction: 1 ,because the value of true is 1 and false is 0
// Actual: 1

console.log (false - true);
// Prediction: -1 , because the value of true is 1 and false is 0
// Actual: -1

console.log (!true);
// Prediction: false , because ! will make the item a boolean
// Actual: false

console.log (3 - 4);
// Prediction: -1, because both item are numbers
// Actual: 

console.log ("Bob" - "bill");
// Prediction: NaN , because the - sign will try to convert the item into numbers 
// Actual: NaN
