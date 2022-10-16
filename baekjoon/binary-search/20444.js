// 입력받기
// let input = require('fs').readFileSync('baekjoon/binary-search/test.txt').toString().trim().split('\n');
let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, k] = input[0].split(' ').map((v) => +v);

// 가로로 자를시에는 기존 개수 + (세로 잘린 수 +1)
// 세로로 자를시에는 기존 개수 + (가로 잘린 수 +1)
function solution(n, k) {
    let answer = 'YES';
    // 가로로 자른 개수
    let lt = 0;
    let rt = n;

    while (lt <= rt) {
        let mid = parseInt((lt + rt) / 2);
        const rowCount = mid;
        const columnCount = n - mid;

        // 60분 기준으로 60/10 + 60/7 = 14명
        let count = (rowCount + 1) * (columnCount + 1);

        if (count === k) {
            return answer;
        }
        // 잘린 개수가 더 많으면 rt를 늘려서 => 가로로 자를 때 기존 개수 + (새로로 잘린수 +1)이기 때문에 세로로 잘린수를 늘리기 위해서 가로로 자른 개수 늘리기
        else if (count > k) {
            rt = mid - 1;
        }
        // 위에 경우와 반대
        else {
            lt = mid + 1;
        }
    }
    answer = 'NO';
    return answer;
}

console.log(solution(parseInt(n), parseInt(k)));
