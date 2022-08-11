console.log("Starting");

let timeout; // ID for the timeout function
function set_timeout(){
  console.log("Setting timeout");

  timeout = setTimeout(function(){
    // Codes to be executed after the timeout
    alert("Today is cold");
  }, 5000); //timeout in milliseconds
}

function clear_timeout() {
  console.log("Clearing timeout");
  clearTimeout(timeout);
}

let interval; // ID for the interval function
let count = 0;
function set_interval() { 
  console.log("Setting interval");
  
  setInterval(function(){
    //Run repeatedly at specific interval
  //   if (count < 3) {
    console.log("Please do not forget to update and send me your project proposal");
  // }
  //   else {
  //     clearInterval(interval);
  //   }
  //   count++;
    }, 5000);

  // stop the function after a spectific time
  setTimeout(function(){
    console.log("Stopping interval");
    clearInterval(interval);
    }, 15000); 

}



function clear_interval() {
  console.log("Clearing interval");
  clearInterval(interval);
}


// Move the box
function move_it(){
  console.log("Moving it");

  let green_box = document.getElementById("outer");
  let golden_box = document.getElementById("inner");
  let green_width = green_box.getBoundingClientRect().width;
  let golden_width = golden_box.getBoundingClientRect().width;

  let pos = 0;
  let move = setInterval(function(){ 

    if (pos > (green_width - golden_width)) {
      clearInterval(move);
    }
    else {
      golden_box.style.left = pos +'px';
      golden_box.style.top = pos +'px';
    }
    pos++;
    
  }, 5)

}