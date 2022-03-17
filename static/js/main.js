const date = new Date()

const monthDays = document.querySelector(".days");

const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
];

function getDaysInMonth (month, year) {
    return new Date(year, month,0).getDate();
}

var currentDate = date.getDate();
var currentMonth = date.getMonth();
var currentYear = date.getFullYear();


function createCalender(){
    let daysInMonth = getDaysInMonth(currentMonth, currentYear);
    let days = "";
    let day = new Date(currentYear, currentMonth,0).getDay();
    for (let i = 0; i < day; i++){
        days += `<li style ="width: 13.6%;"> ____________ </li>`;
    }
    for (let i = 1; i <= daysInMonth; i++) {
        if (i == currentDate){
            days += `<li class = "current" onclick = "selectdate(this)">${i}</li>`;
        }else{
            days += `<li class = "normal" onclick = "selectdate(this)">${i}</li>`;
        }
    }

    monthDays.innerHTML = days;
}

function selectdate(element){
    let oldElement = document.getElementsByClassName("current");
    console.log(oldElement);
    oldElement[0].className = "normal";

    element.className = "current" ;
    let currentDate = element.innerHTML;
    console.log(currentDate);
    
    
}

function nextMonth(){
    currentMonth++;
}

function previousMonth(){
    currentMonth--;
}

function nextYear(){
    currentYear++;
}

function previousYear(){
    currentYear--;
}


createCalender();

function book(){
    let day = document.getElementsByClassName("current")[0].innerHTML
    console.log(day)
    let date = new Date(currentYear, currentMonth,day)
    let dj = document.getElementById("currentDj").innerHTML
    date = getFormattedDate(date)
    window.location.replace("/book/confirm/book?dj="+dj+"&date="+date);
}

function getFormattedDate(date) { //function from https://stackoverflow.com/questions/11591854/format-date-to-mm-dd-yyyy-in-javascript
    var year = date.getFullYear();

    var month = (1 + date.getMonth()).toString();
    month = month.length > 1 ? month : '0' + month;

    var day = date.getDate().toString();
    day = day.length > 1 ? day : '0' + day;
    
    return year + '-' + month + '-' + day ;
}