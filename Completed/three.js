/*
    https://projecteuler.net/problem=3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    This can be made much more efficent by use of Sieve of Erathenos however this problem didnt need it so I waited till another to
    implement it
    Checks if factor then checks if factor is prime then adds to array
*/


var numberToFactor = 600851475143;
var factors = [];
getFactor(numberToFactor);
console.log(factors);
function getFactor(numToFac){
    for(var i = 2; i < numToFac; i++){
        if(numToFac % i == 0 && checkPrime(i) == true){
            factors.push(i);
            getFactor((numToFac / i));
            return;
        }
    }
    factors.push(numToFac);
}

function checkPrime(num){
    for(var i = 2; i < num - 1; i++){
        if(num % i == 0){
            return false;
        }
    }
    return true;
}