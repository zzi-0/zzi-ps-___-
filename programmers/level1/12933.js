function solution(n) {
    let answer = [];

    const numberArray = String(n).split('').sort();
    while (numberArray.length) {
        answer.push(Math.max(...numberArray));
        numberArray.pop();
    }

    return parseInt(answer.join(''));
}

console.log(solution(118372));
