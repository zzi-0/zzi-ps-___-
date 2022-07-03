function getDistance(number, beforeHand) {
    let numberMapping = new Map();

    numberMapping.set(1, [0, 0]);
    numberMapping.set(2, [0, 1]);
    numberMapping.set(3, [0, 2]);
    numberMapping.set(4, [1, 0]);
    numberMapping.set(5, [1, 1]);
    numberMapping.set(6, [1, 2]);
    numberMapping.set(7, [2, 0]);
    numberMapping.set(8, [2, 1]);
    numberMapping.set(9, [2, 2]);
    numberMapping.set('*', [3, 0]);
    numberMapping.set(0, [3, 1]);
    numberMapping.set('#', [3, 2]);

    return (
        Math.abs(numberMapping.get(number)[0] - numberMapping.get(beforeHand)[0]) +
        Math.abs(numberMapping.get(number)[1] - numberMapping.get(beforeHand)[1])
    );
}

function solution(numbers, hand) {
    var answer = '';
    let leftHand = '*';
    let rightHand = '#';
    for (const number of numbers) {
        if (number === 1 || number === 4 || number === 7) {
            answer += 'L';
            leftHand = number;
        } else if (number === 3 || number === 6 || number === 9) {
            answer += 'R';
            rightHand = number;
        } else {
            if (getDistance(number, leftHand) > getDistance(number, rightHand)) {
                answer += 'R';
                rightHand = number;
            } else if (getDistance(number, leftHand) < getDistance(number, rightHand)) {
                answer += 'L';
                leftHand = number;
            } else {
                if (hand === 'right') {
                    answer += 'R';
                    rightHand = number;
                } else {
                    answer += 'L';
                    leftHand = number;
                }
            }
        }
    }
    return answer;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'));
