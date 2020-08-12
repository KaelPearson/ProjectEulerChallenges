var grid = [
    [], // 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
];

var height = 20;
var width = 20;

createGrid();
console.log(getHighest());

function getHighest(){
    var diag = findHighestDiagonal();
    var up = findHighestUp();
    var left = findHighestLeft();
    var otherDiag = findHighestOtherDiagonal();
    if(diag > up && diag > left && diag > otherDiag){
        return diag;
    } else if (up > diag && up > left && up > otherDiag){
        return up
    } else if (left > diag && left > up && left > otherDiag){
        return left;
    } else {
        return otherDiag;
    }
}
function findHighestDiagonal(){
    var highest = 0; 
    var highestArr = [];
    for(var i = 0; i < height - 4; i++){
        for(var k = 0; k < width - 4; k++){
            var arr = [];
            arr.push(grid[i][k]);
            arr.push(grid[i + 1][k + 1]);
            arr.push(grid[i + 2][k + 2]);
            arr.push(grid[i + 3][k + 3]);
            if(getProduct(arr) > highest){
                highest = getProduct(arr);
                highestArr = arr;
            }
        }
    }
    return highest;
}
function findHighestOtherDiagonal(){
    var highest = 0;
    var highestArr = [];
    for(var i = 3; i < height; i++){
        for(var k = 0; k < width - 3; k++){
            var arr = [];
            arr.push(grid[i][k]);
            arr.push(grid[i - 1][k + 1]);
            arr.push(grid[i - 2][k + 2]);
            arr.push(grid[i - 3][k + 3]);
            if(getProduct(arr) > highest){
                highest = getProduct(arr);
                highestArr = arr;
            }
        }
    }
    return highest;
}
function findHighestUp(){
    var highest = 0;
    var highestArr = [];
    for(var i = 0; i < height - 4; i++){
        for(var k = 0; k < width; k++){
            var arr = [];
            arr.push(grid[i][k]);
            arr.push(grid[i+1][k]);
            arr.push(grid[i+2][k]);
            arr.push(grid[i+3][k]);
            if(getProduct(arr) > highest){
                highest = getProduct(arr);
                highestArr = arr;
            }
        }
    }
    return highest;
}

function findHighestLeft(){
    var highest = 0;
    var highestArr = [];
    for(var i = 0; i < height; i++){
        for(var k = 0; k < width - 4; k++){
            var arr = [];
            arr.push(grid[i][k]);
            arr.push(grid[i][k+1]);
            arr.push(grid[i][k+2]);
            arr.push(grid[i][k+3]);
            if(getProduct(arr) > highest){
                highest = getProduct(arr);
                highestArr = arr;
            }
        }
    }
    return highest;
}



function createGrid(){
    var rows = [
        "0802229738150040007504050778521250779108",
        "4949994017811857608717409843694804566200",
        "8149317355791429937140675388300349133665",
        "5270952304601142692468560132567137023691",
        "2231167151676389419236542240402866331380",
        "2447326099034502447533537836842035171250",
        "3298812864236710263840675954706618386470",
        "6726206802621220956394396308409166499421",
        "2455580566739926971778789683148834896372",
        "2136230975007644204535140061339734313395",
        "7817532822753167159403800462161409535692",
        "1639054296353147555888240017542436298557",
        "8656004835718907054444374460215851541758",
        "1980816805944769287392138652177704895540",
        "0452088397359916079757321626267933279866",
        "8836688757622072034633674655123263935369",
        "0442167338253911249472180846293240627636",
        "2069364172302388346299698267598574043616",
        "2073352978319001743149714886811623570554",
        "0170547183515469169233486143520189196748"
    ];
    for(var i = 0; i < height; i++){
        for(var k = 0; k < width * 2; k += 2){
            var num1 = rows[i][k];
            var num2 = rows[i][k+1];
            var value = num1 + num2;
            grid[i][k / 2] = value;
        }
    }
}

function getProduct(arr){
    var total = 1;
    for(var i = 0; i < arr.length; i++){
        total *= parseInt(arr[i]);
    }
    return total;
}