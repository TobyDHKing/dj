const date = new Date()

var currentMonth = date.getMonth();
var currentYear = date.getFullYear();

const monthDays = document.querySelector(".days");
const monthYear = document.getElementById("monthYear") // get the month year element from html page

function getDaysInMonth (month, year) { // get days in the month
    return new Date(year, month+1,0).getDate();
}

function getFormattedDate(date) { //function from https://stackoverflow.com/questions/11591854/format-date-to-mm-dd-yyyy-in-javascript
    var year = date.getFullYear();

    var month = (1 + date.getMonth()).toString(); 
    month = month.length > 1 ? month : '0' + month; 

    var day = date.getDate().toString();
    day = day.length > 1 ? day : '0' + day;
    
    return year + '-' + month + '-' + day ;
}

const month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

function createCalender(){
    monthDays.innerHTML = "" // clear old calender
    let daysInMonth = getDaysInMonth(currentMonth, currentYear); // get days in month to loop through
    let days = "";
    let day = new Date(currentYear, currentMonth,0).getDay();
    // this is used to create empty elements for the days of the week that arnt in the month
    for (let i = 0; i < day; i++){ // loop up until the first day of the month in in the week
        days += `<li style ="width: 13.6%;"> ____________ </li>`; // create empty element 
    }
    for (let i = 1; i <= daysInMonth; i++) { //loop through days in month and create the list of elements
        if (i == 2){
            days += `<li class = "current" onclick = "selectdate(this)">${i}</li>`; //set 2nd day to current day
        }else{
            days += `<li class = "normal" onclick = "selectdate(this)">${i}</li>`;
        }
    }
    
    monthDays.innerHTML = days; // set inner html of th

    
    monthYear.innerHTML = month[currentMonth]+'<br><span style="font-size:18px">'+currentYear+'</span>' // using the currentmonth get the name using array and set html
}

function selectdate(element){
    let oldElement = document.getElementsByClassName("current"); //select day is ran when element is clicked
    oldElement[0].className = "normal"; //set old element to normal
    element.className = "current" ; // set element clicked to active
}

function nextMonth(){
    if (currentMonth == 11){ // limit currentMonth to 0, month is 0 indexed so 11 is max rather than 12
        return
    }
    currentMonth++;
    createCalender(); // recreate calender
}

function previousMonth(){
    if (currentMonth == 0) { // limit currentMonth to 0, month is 0 indexed
        return
    }
    currentMonth--;
    createCalender(); // recreate calender
}

function nextYear(){
    currentYear++;
    createCalender();
}

function previousYear(){
    currentYear--;
    createCalender();
}


createCalender();

function book(){
    let day = document.getElementsByClassName("current")[0].innerHTML // get current day
    let date = new Date(currentYear, currentMonth,day)
    let dj = document.getElementById("currentDj").innerHTML // get dj
    date = getFormattedDate(date) // formats date
    window.location.replace("/book/confirm/book?dj="+dj+"&date="+date); // send request using data from page
}

