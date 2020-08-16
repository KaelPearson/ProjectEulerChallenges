/*
    https://projecteuler.net/problem=10
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

    This is the program that needed to have Sieve of Eratosthenes as otherwise it would take forever
    I set the value of list[i] = 0 because removing from list causes huge amount of time 
*/

var highest = 2000000;

console.log(sieve(highest));
function sieve(limit){
    var list = [];
    for(var i = 2; i <= limit; i++){
        list.push(i);
    }
    var count = 2;
    while(count < Math.sqrt(limit)){
        for(var i = count - 1; i < list.length; i++){
            if(list[i] % count == 0){
                list[i] = 0;
            }
        }
        count++;
    }
    var sum = 0;
    for(var i = 0; i < list.length; i++){
        sum += list[i];
    }
    return sum;
}