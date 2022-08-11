console.log("Starting");

// let planets = [
//   'Mercury',
//   'Venus',
//   'Earth',
//   'Mars',
//   'Jupiter',
//   'Saturn',
//   'Uranus',
//   'Neptune'
// ];

// let section = document.getElementsByTagName('section')[0];
// for (let planet of planets) {
//   let div = document.createElement('div');
//   div.className = 'planet';
//   div.classList.add(planet);
//   div.textContent = planet;

//   section.appendChild(div);
// }

//Bonus Section

let planets_2 = {
  Mercury: ['moon', 'moon'],
  Venus: ['moon'],
  Earth: ['moon'],
  Mars: ['moon'],
  Jupiter: ['moon', 'moon'],
  Saturn: ['moon', 'moon','moon'],
  Uranus: ['moon', 'moon'],
  Neptune: ['moon'],
}

let section = document.getElementsByTagName('section')[0];
for (let key in planets_2) {
  let planet_div = document.createElement('div');
  planet_div.className = 'planet';
  planet_div.classList.add(key);
  planet_div.textContent = key;

  // Add the moons for each planet
  let count = 3;
  for (let moon of planets_2[key]) {
    let moon_div = document.createElement('div');
    moon_div.className = 'moon';
    moon_div.style.left = (60* count).toString() + 'px';
    planet_div.appendChild(moon_div);
    count++;

  }


  section.appendChild(planet_div);
}