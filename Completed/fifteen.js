/*
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


    How many such routes are there through a 20×20 grid?

    Used size! * 2 / size! * size!
    to find amount of paths
*/


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