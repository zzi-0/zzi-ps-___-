function solution(dartResult) {
    let answer = [];

    for (let i = 0; i < dartResult.length; i++) {
        if (dartResult[i] === 'S') {
            if (dartResult[i - 2] === '1' && dartResult[i - 1] === '0') answer.push(10);
            else answer.push(Number(dartResult[i - 1]));
        } else if (dartResult[i] === 'D') {
            if (dartResult[i - 2] === '1' && dartResult[i - 1] === '0') answer.push(100);
            else answer.push(Math.pow(Number(dartResult[i - 1]), 2));
        } else if (dartResult[i] === 'T') {
            if (dartResult[i - 2] === '1' && dartResult[i - 1] === '0') answer.push(1000);
            else answer.push(Math.pow(Number(dartResult[i - 1]), 3));
        } else if (dartResult[i] === '*') {
            answer[answer.length - 1] *= 2;
            answer[answer.length - 2] *= 2;
        } else if (dartResult[i] === '#') {
            answer[answer.length - 1] *= -1;
        }
    }
    return answer.reduce((sum, num) => (sum += num));
}

console.log(solution('1D#2S*3S'));
