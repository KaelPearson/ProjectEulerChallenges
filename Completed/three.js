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