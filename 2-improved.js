let first_num = 2;
let second_num = 3;
let sum = sum_of_args(first_num, second_num);

function sum_of_args() {
    let sum = 0;
    for (i of arguments) {
        sum += i;

    } return sum;
}

console.log(sum);





