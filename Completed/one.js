/*
    https://projecteuler.net/problem=1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

    Originally done for interview question used simple modulus to complete
*/

var numberToSum = 1000;
var num1 = 3;
var num2 = 5;

var total = 0;
for(var i = 0; i < numberToSum; i++){
    if(i % num1 == 0 || i % num2 == 0){
        total += i;
    }
}
console.log(total);