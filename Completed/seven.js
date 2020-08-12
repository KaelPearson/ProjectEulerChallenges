
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