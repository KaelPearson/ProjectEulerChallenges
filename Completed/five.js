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