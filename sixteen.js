var number = 2;
var pow = 1000;


// May need to switch languages for this problem as javascript doesnt like very large numbers
// python has pow() function which will return as a integer allowing for easier use

console.log(sumOfDigits());
function sumOfDigits(){
    var num = Math.pow(number,pow);
    var str = num.toString();
    var sum = 0;
    for(var i = 0; i < str.length; i++){
        sum += parseInt(str[i]);
    }
    return str;
}