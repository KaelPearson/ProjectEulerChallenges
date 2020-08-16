/*
    https://projecteuler.net/problem=19
    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

    Pretty straight forward figure out days between each sunday and try to figure out from that
*/

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