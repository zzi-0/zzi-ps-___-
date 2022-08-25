function solution(numbers) {
    var answer = [];
    numbers.forEach((number) => {
        if (number % 2 === 0) answer.push(number + 1);
        else {
            let numberBit = '0' + number.toString(2);
            for (let i = numberBit.length - 1; i >= 0; i--) {
                if (numberBit[i] === '0') {
                    numberBit = numberBit.substring(0, i) + '10' + numberBit.substring(i + 2, numberBit.length);
                    answer.push(parseInt(numberBit, 2));
                    break;
                }
            }
        }
    });
    return answer;
}

console.log(solution([2, 7]));
