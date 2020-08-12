var highest = 100;
var lowest = 1;
console.log(getDifference());
function getDifference(){
    return getSquareOfSum() - getSumOfSquares();
}
function getSumOfSquares(){
    var total = 0;
    for(var i = lowest; i <= highest; i++){
        total += i*i;
    }
    return total;
}

function getSquareOfSum(){
    var total = 0;
    for(var i = lowest; i <= highest; i++){
        total += i;
    }
    return total * total;
}