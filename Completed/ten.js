var highest = 2000000;

console.log(sieve(highest));
function sieve(limit){
    var list = [];
    for(var i = 2; i <= limit; i++){
        list.push(i);
    }
    var count = 2;
    while(count < Math.sqrt(limit)){
        for(var i = count - 1; i < list.length; i++){
            if(list[i] % count == 0){
                list[i] = 0;
            }
        }
        count++;
    }
    var sum = 0;
    for(var i = 0; i < list.length; i++){
        sum += list[i];
    }
    return sum;
}