var currYear = 1901;
var currDay = 1;
var currMonth = 1;

var monthDayAmount = [31,28,31,30,31,30,31,31,30,31,30,31];

amountOfSundays();
function amountOfSundays(){
    var startingDays = getStartingDay();
    var count = 0;
    for(var i = 0; i < startingDays.length; i++){
        if(startingDays[i] % 7 == 0){
            count++;
        }
    }
    console.log(count);
}
function getStartingDay(){
    var startingDays = [];
    for(var i = currYear; i <= 2000; i++){
        if(i % 4 == 0){
            i[1] = 29;
        } else {
            i[1] = 28;
        }
        for(var k = 0; k < monthDayAmount.length; k++){
            startingDays.push(currDay);
            currDay += monthDayAmount[k]
        }
    }
    return startingDays;
}