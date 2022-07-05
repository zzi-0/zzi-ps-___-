function getBinary(n, number) {
    let binary = Array.from({ length: n }, () => 0);
    let index = n - 1;

    while (number > 0) {
        binary[index] = parseInt(number % 2);
        number = parseInt(number / 2);
        index--;
    }
    return binary;
}

function solution(n, arr1, arr2) {
    var answer = [];
    let arr1Binary = [];
    let arr2Binary = [];
    for (const num of arr1) {
        arr1Binary.push(getBinary(n, num));
    }
    for (const num of arr2) {
        arr2Binary.push(getBinary(n, num));
    }

    for (let i = 0; i < n; i++) {
        let row = '';
        for (let j = 0; j < n; j++) {
            if (arr1Binary[i][j] === 0 && arr2Binary[i][j] === 0) row += ' ';
            else row += '#';
        }
        answer.push(row);
    }

    return answer;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
