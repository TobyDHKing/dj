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
    for (let i = 1; i <= daysInMonth; i++) {
        if (i == currentDate){
            days += `<div class = "current" onclick = "selectdate(this)">${i}</div>`;
        }else{
            days += `<div class = "normal" onclick = "selectdate(this)">${i}</div>`;
        }
        
    }

    monthDays.innerHTML = days;
}

function selectdate(element){
    let oldElement = document.getElementsByClassName("current");
    console.log(oldElement)
    oldElement[0].className = "normal";

    element.className = "current" ;
    let currentDate = element.innerHTML;
    console.log(currentDate)
    
    
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