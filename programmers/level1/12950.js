function solution(arr1, arr2) {
    let answer = [];
    for (let i = 0; i < arr1.length; i++) {
        let sum = [];
        for (let j = 0; j < arr1[i].length; j++) {
            sum.push(parseInt(arr1[i][j]) + parseInt(arr2[i][j]));
        }
        answer.push(sum);
    }
    return answer;
}

console.log(solution([[1], [2]], [[3], [4]]));
