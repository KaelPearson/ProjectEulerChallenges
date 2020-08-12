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