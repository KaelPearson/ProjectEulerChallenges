var numberToSum = 1000;
var num1 = 3;
var num2 = 5;

var total = 0;
for(var i = 0; i < numberToSum; i++){
    if(i % num1 == 0 || i % num2 == 0){
        total += i;
    }
}
console.log(total);