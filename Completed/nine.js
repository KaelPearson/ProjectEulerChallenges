/* 
    https://projecteuler.net/problem=9
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a2 + b2 = c2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc. 

    check every triplet
*/

// up c check all possible
var answer = 1000;

console.log(getTriplet());

function getTriplet(){
    var a = 1;
    var b = 2;
    var c = 3;
    while(true){
        if(checkTriplet(a,b,c) == true){
            break;
        }
        if(a+1 < b){
            a++;
        } else if(b+1 < c){
            b++;
            a = 1;
        } else {
            c++;
            b = 1;
            a = 1;
        }
    }
    return "a " + a + " b " + b + " c "+ c;
}
function checkTriplet(a,b,c){
    var newA = a * a;
    var newB = b * b;
    var newC = c * c;
    if(newA + newB == newC){
        if(a + b + c == 1000) {
            return true;
        }
    }
    return false;
}