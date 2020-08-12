var size = 20;
getLetticePath();
function getLetticePath(){
    var total = getFactorial(size * 2);
    total /= getFactorial(size) * getFactorial(size);
    console.log(total);
}

function getFactorial(num){
    var total = 1;
    for(var i = 2; i <= num; i++){
        total *= i;
    }
    return total;
}