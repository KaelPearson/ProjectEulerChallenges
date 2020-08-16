/*
    https://projecteuler.net/problem=5
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    forever while loop till it find smallest number that dividesIntoAll as seen in that function
    Not good because the while loop doesnt ever have a break point so it might be possible to get stuck in

*/
var lowest = 2;
var highest = 20;
console.log(smallestMultiple());
function smallestMultiple(){
    var numToCheck = 1;
    while(dividesIntoAll(numToCheck) == false){
        numToCheck++;
    }
    return numToCheck;
}
function dividesIntoAll(numToCheck){
    for(var i = lowest; i < highest; i++){
        if(numToCheck % i != 0){
            return false;
        }
    }
    return true;
}