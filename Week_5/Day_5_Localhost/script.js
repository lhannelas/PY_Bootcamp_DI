let input = document.getElementById('input');
let submit = document.getElementById('submit');
let retrieve = document.getElementById('retrieve');
let output = document.getElementById('output');
let clear = document.getElementById('clear');

submit.addEventListener('click', function () {
  console.log('submitted');

  //Highscore example [1.only highest score, 2. Top 5 scores]
  let current_hs = localStorage.getItem('input');
  if (current_hs === null){
    localStorage.setItem('input', input.value);
  }

  //1. only Highest score
  // else if (input.value > Number(current_hs)) {
  //    alert("NEW HIGHSCORE");
  //    localStorage.setItem('input', input.value);
  //}
  //else{
  //  console.log("No new higscore");
  //}

  else{ //2. Top 5 scores
    let hs_str = input.value + ',' + current_hs;
    let hs_arr = hs_str.split(',');
    // let hs_arr_num = []
    // hs_arr.forEach(num => hs_arr_num.push(Number(num)));
    let hs_desc = hs_arr.sort((a,b)=>b-a); //b-a converts to number
    let hs_top_5 = hs_desc.slice(0,5);
    console.log(hs_top_5);
    localStorage.setItem('input', hs_top_5.toString());      
  }
})
  


retrieve.addEventListener('click', function () {
  console.log('submitted');

  let input_value = localStorage.getItem('input');
  console.log(input_value);// numm if key does not exist
  console.log(input_value);
});

clear.addEventListener('click', function () {
  console.log('clear');

});