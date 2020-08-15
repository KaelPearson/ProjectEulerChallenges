var numToFactorial = 100;

console.log(getTotalOfDigits(getFactorial(numToFactorial)));

// Issue with very big nums
// Use diff language?

function getTotalOfDigits(str){
    var sum = 0;
    for(var i = 0; i < str.length; i++){
        sum += parseInt(str[i]);
    }
    return sum;
}
function getFactorial(num){
    var sum = 1;
    for(var i = 1; i <= num; i++){
        sum *= i;
    }
    return sum.toString();
}