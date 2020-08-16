/*
    https://projecteuler.net/problem=6
    The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is . 3025 - 385 = 2640

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

    Problem is pretty easy to understand getSumOfSquares and getSquareOfSum and subtract them return value
*/

var highest = 100;
var lowest = 1;
console.log(getDifference());
function getDifference(){
    return getSquareOfSum() - getSumOfSquares();
}
function getSumOfSquares(){
    var total = 0;
    for(var i = lowest; i <= highest; i++){
        total += i*i;
    }
    return total;
}

function getSquareOfSum(){
    var total = 0;
    for(var i = lowest; i <= highest; i++){
        total += i;
    }
    return total * total;
}