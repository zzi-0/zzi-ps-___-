function solution(arr) {
    var answer = [];
    let beforeNumber = arr[0];

    answer.push(arr[0]);
    for (let i = 1; arr.length > i; i++) {
        if (arr[i] !== beforeNumber) answer.push(arr[i]);
        beforeNumber = arr[i];
    }

    return answer;
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]));
