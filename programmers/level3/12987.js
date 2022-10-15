// 작은 것 부터 체크하면 됨
function solution(a, b) {
    let answer = 0;
    let i = 0;
    let j = 0;

    a.sort((a, b) => a - b);
    b.sort((a, b) => a - b);

    while (j !== b.length) {
        if (a[i] < b[j]) {
            i++;
            j++;
            answer++;
        } else {
            j++;
        }
    }

    return answer;
}

console.log(solution([2, 2, 2, 3], [2, 2, 2, 3]));
console.log(solution([5, 1, 3, 7], [2, 2, 6, 8]));
console.log(solution([2, 2, 2, 2], [1, 1, 1, 1]));
