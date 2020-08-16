/*
    https://projecteuler.net/problem=7
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?

    bruteForced could be optimized by sieve of Eratosthenes
*/

console.log(getPrimeNum(10001));
function getPrimeNum(spot){
    var primeCount = 0;

    var currNum = 2;
    while(spot != primeCount){
        if(checkPrime(currNum) == true){
            primeCount++;
        }
        currNum++;
    }
    return currNum - 1;
}


function checkPrime(num){
    for(var i = 2; i < num - 1; i++){
        if(num % i == 0){
            return false;
        }
    }
    return true;
}