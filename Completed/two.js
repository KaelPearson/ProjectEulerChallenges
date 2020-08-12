/* var term1 = 0;
var term2 = 1;

for(var i = 0; i < 8; i++){
    newTerm = term1 + term2;
    console.log(newTerm);
    oldTerm1 = term1;
    term1 = term2;
    term2 = oldTerm1 + term2;
} */


var total = 0;
var num1 = 0;
var num2 = 1;
var limit = 4000000;
while(true){
    if(num1 + num2 > limit){
        break;
    }
    if((num1 + num2) % 2 == 0){
        total += num1 + num2;
    }
    oldNum1 = num1;
    num1 = num2;
    num2 = oldNum1 + num2;
}
console.log(total);