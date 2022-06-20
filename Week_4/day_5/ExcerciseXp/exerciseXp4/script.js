console.log("books");

let allbooks = {title: "",
                author:"",
                image: "",
                alreadyRead:""};

let firstBook = {title: "RichDadPoorDad",
                 author: "Robert Kiyosaki",
                 image: "https://kbimages1-a.akamaihd.net/ddf8d53d-7df5-4560-8fbd-43915f4f6a03/353/569/90/False/rich-dad-poor-dad-24.jpg/",
                 alreadyRead:true}

let secondBook = {title: "The Richest man in Babylone",
                  author: "George Clason",
                  image: "https://m.media-amazon.com/images/I/51pYZS7IWcL.jpg",
                  alreadyRead:true}


let body = document.body;
let div = document.body.firstElementChild;
console.log(div);

let table = document.createElement("table");
// table.textContent = "ggt";
div.appendChild(table);
table.style.border = "1px solid black";

let tr1 = document.createElement("tr");
// tr.textContent = "1";
table.appendChild(tr1);


let th1 = document.createElement("th");
th1.textContent = "Book";
tr1.appendChild(th1);
th1.style.border = "1px solid black";

let th2 = document.createElement("th");
th2.textContent = "Author";
tr1.appendChild(th2);
th2.style.border = "1px solid black";

let th3 = document.createElement("th");
th3.textContent = "image";
tr1.appendChild(th3);
th3.style.border = "1px solid black";

let tr2 = document.createElement("tr");
table.appendChild(tr2);

let td1 = document.createElement("td");
td1.textContent = firstBook.title;
tr2.appendChild(td1);
td1.style.border = "1px solid black";
// td1.style.color = "red";

let td2 = document.createElement("td");
td2.textContent = firstBook.author;
tr2.appendChild(td2);
td2.style.border = "1px solid black";

let td3 = document.createElement("td");
tr2.appendChild(td3);
td3.style.border  = "1px solid black";

let image1 = document.createElement("img");
image1.src = firstBook.image;
td3.appendChild(image1);
image1.style.width = "100px";

let tr3 = document.createElement("tr");
table.appendChild(tr3);

let td4 = document.createElement("td");
td4.textContent = secondBook.title;
tr3.appendChild(td4);
td4.style.border = "1px solid black";

let td5 = document.createElement("td");
td5.textContent = secondBook.author;
tr3.appendChild(td5);
td5.style.border = "1px solid black";

let td6 = document.createElement("td");
tr3.appendChild(td6);
td6.style.border  = "1px solid black";

let image2 = document.createElement("img");
image2.src = secondBook.image;
td6.appendChild(image2);
image2.style.width = "100px";

console.log(firstBook.alreadyRead);
if (firstBook.alreadyRead === true) {
  td1.style.color = "red";
}

if (secondBook.alreadyRead === true) {
  td4.style.color = "red";
}
