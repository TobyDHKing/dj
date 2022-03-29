const date = new Date()

const monthDays = document.querySelector(".days");

function getDaysInMonth (month, year) {
    return new Date(year, month+1,0).getDate();
}

const month = ["January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December"];


var currentDate = date.getDate();
var currentMonth = date.getMonth();
var currentYear = date.getFullYear();
date.getMonth()

function createCalender(){
    monthDays.innerHTML = ""
    let daysInMonth = getDaysInMonth(currentMonth, currentYear);
    console.log(currentMonth,currentYear)
    let days = "";
    let day = new Date(currentYear, currentMonth,0).getDay();
    console.log(day)
    for (let i = 0; i < day; i++){
        days += `<li style ="width: 13.6%;"> ____________ </li>`;
    }
    console.log("here")
    console.log('curdate: ',currentDate)
    for (let i = 1; i <= daysInMonth; i++) {
        console.log('also here')
        if (i == currentDate){
            
            console.log('set current')
            days += `<li class = "current" onclick = "selectdate(this)">${i}</li>`;
        }else{
            days += `<li class = "normal" onclick = "selectdate(this)">${i}</li>`;
        }
    }
    
    monthDays.innerHTML = days;

    monthYear = document.getElementById("monthYear")
    monthYear.innerHTML = month[currentMonth]+'<br><span style="font-size:18px">'+currentYear+'</span>'
}

function selectdate(element){
    console.log("here")
    let oldElement = document.getElementsByClassName("current");
    console.log(oldElement);
    oldElement[0].className = "normal";

    element.className = "current" ;    
}

function nextMonth(){
    currentMonth++;
    createCalender();
}

function previousMonth(){
    currentMonth--;
    createCalender();
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