//Exercise 1
 console.log (5 >= 1);
//Prediction : True , The items are boolean and 5 is greater than 1
//Actual : true

 console.log (0 === 1);
//Prediction : False , The items are boolean and the items do have the same value
//Actual : false

 console.log (4 <= 1);
//Prediction : false , The items are boolean and 4 is greater than 1
//Actual : false

console.log (1 != 1);
//Prediction : false , The items are boolean and 1 is equal to 1
//Actual : false

console.log ("A" > "B");
//Prediction : false , The items are boolean and A=065 is smaller than B =066
//Actual : false

console.log ("B" < "C");
//Prediction : true , The items are boolean and B=066 is smaller than C =067
//Actual : true

console.log ("a" > "A");
//Prediction : true , The items are boolean and a=097 is greater than A =065
//Actual : true

console.log ("b" < "A");
//Prediction : false , The items are boolean and b=098 is greater than A =065
//Actual : false

console.log (true === false);
//Prediction : false , The items have same boolean type but true=1 and false=0 
//Actual : false

console.log (true != true);
//Prediction : false , The items are boolean and have same value
//Actual : false

//Exercise 2
let str = prompt("Enter some numbers" , "2, 15, 6");

let citrus = str.toString()