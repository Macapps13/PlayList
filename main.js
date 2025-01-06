var now = new Date()
switch (now.getDay()) {
    case 0:
      day = "Sunday";
      break;
    case 1:
      day = "Monday";
      break;
    case 2:
       day = "Tuesday";
      break;
    case 3:
      day = "Wednesday";
      break;
    case 4:
      day = "Thursday";
      break;
    case 5:
      day = "Friday";
      break;
    case 6:
      day = "Saturday";
  }
var year = now.getFullYear();
var month = now.getMonth();
var date = now.getDate(); 

document.getElementById("today").innerHTML = "Today is " + day + ", " + date + "/" + (month+1) + "/" + year;