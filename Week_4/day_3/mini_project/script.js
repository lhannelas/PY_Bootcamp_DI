console.log("Play the game!")

function playTheGame(){
    // console.log("button clicked!");
    let answer = confirm("Would you like to play the game?");

    if (answer === false){ // if (!answer)
        alert("No problem, Goodbye!");
    }
    else if (answer){
        // Continue with the game

        // let num = prompt("Please enter a number between 0 and 10");
        // num = Number(num);
        //
        // if (isNaN(num)){
        //     alert("Sorry Not a number, Goodbye");
        // }
        // else if (num < 0 || num > 10){
        //     alert("Sorry it's not a good number, Goodbye");
        // }

        let userNumber = askUserNumber();

        if (!isNaN(userNumber)){
        // else{
            let computerNumber = randNum(10);
            console.log("Computer Number: " + computerNumber);
            compareNumbers(userNumber, computerNumber);
        }
    }
}

function randNum(max){
    return Math.round(Math.random() * max)
    // with min max:
    // console.log(Math.round(Math.random() * (max-min) + min ))
}

function compareNumbers(userNumber, computerNumber){
    let win = false;

    for (let i = 1; i <= 3; i++) {
        if (userNumber === computerNumber) {
            alert("WINNER");
            win = true;
            break;
        } else if (userNumber > computerNumber) {
            alert("Your number is bigger than the computer’s, guess again");
            if (i < 3) {
                userNumber = askUserNumber();
            }
        } else if (userNumber < computerNumber) {
            alert("Your number is smaller than the computer’s, guess again");
            if (i < 3) {
                userNumber = askUserNumber();
            }
        }
    }

    if (!win){
        alert("Out of chances!");
    }
}

function askUserNumber(){
    let num = prompt("Please enter a number between 0 and 10");
    num = Number(num);

    // Bonus Part ####
    while(isNaN(num) || num < 0 || num > 10 ){
        alert("Sorry not a number or number is out of range, please try again...");
        num = prompt("Please enter a number between 0 and 10");
        num = Number(num);
    }
    // ##########

    // if (isNaN(num)){
    //     alert("Sorry Not a number, Goodbye");
    //     return NaN;
    // }
    // else if (num < 0 || num > 10){
    //     alert("Sorry it's not a good number, Goodbye");
    //     return NaN;
    // }

    return num;
}