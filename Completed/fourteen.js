/*
    https://projecteuler.net/problem=14
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.

    Checks all numbers under one million compares changes
*/

var amountOfNumbersToCheck = 1000000;

console.log(longestProblem());
function longestProblem(){
    var startingNum = 1;
    var currNum = startingNum;

    var highestChanges = 0;
    var highestStartingNum = 0;
    var amountOfChanges = 1;
    for(var i = 1; i < amountOfNumbersToCheck; i++){
        while(currNum != 1){
            if(currNum % 2 == 0){
                currNum /= 2;
            } else {
                currNum = (3 * currNum) + 1;
            }
            amountOfChanges++;
        }
        
        if(amountOfChanges > highestChanges){
            highestChanges = amountOfChanges;
            highestStartingNum = startingNum;
        }
        startingNum++;
        currNum = startingNum;
        amountOfChanges = 1;
    }

    return highestStartingNum;
}