var highest = 999;
var lowest = 100;
console.log(getBiggestPalindrone());
function getBiggestPalindrone(){
    var biggestPalindrone = 0;
    for(var i = lowest; i <= highest; i++){
        for(var k = i; k <= highest; k++){
            var numToCheck = k * i;
            if(numToCheck > biggestPalindrone && isPalindrome(String(numToCheck)) == true){
                biggestPalindrone = numToCheck;
            }
        }
    }
    return biggestPalindrone;
}

function isPalindrome(check){
    var length = check.length;
    var firstHalf = "";
    for(var i = 0; i < length / 2; i++){
        firstHalf += check[i];
    }
    var secondHalf = "";
    for(var i = length - 1; i >= length / 2; i--){
        secondHalf += check[i];
    }
    for(var i = 0; i < secondHalf.length; i++){
        if(firstHalf[i] != secondHalf[i]){
            return false;
        }
    }
    return true;
}