var amount = 500;
console.log(getOverDivisors(amount));


function getOverDivisors(count){
    var currTrig = 1;
    var amountToUp = 2;
    while(getAmountOfDivisors(currTrig) < count){
        currTrig += amountToUp;
        amountToUp++;
    }
    return currTrig;
}

function getAmountOfDivisors(num){
    amount = 2;
    if(num % 2 == 0){
        amount += 2;
    }
    for(var i = 3; i <= Math.sqrt(num); i++){
        if(num % i == 0){
            if(num / i == i){
                amount++;
            } else {
                amount += 2;
            }
        }
    }
    return amount;
}