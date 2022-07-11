const isPrime = (num) => {
    if (num === 1 || num === 0) return false;
    for (let i = 2; i < num; i++) {
        if (num % i === 0) return false;
    }
    return true;
};

const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);

    arr.forEach((fixed, index, origin) => {
        const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
        const permutations = getPermutations(rest, selectNumber - 1);
        const attached = permutations.map((el) => [fixed, ...el]);
        results.push(...attached);
    });

    return results;
};

function solution(numbers) {
    let answer = 0;
    const numArr = numbers.split('').map((number) => parseInt(number));
    let possibleNumArr = [];
    for (let i = 1; i <= numArr.length; i++) {
        getPermutations(numArr, i).map((num) => {
            possibleNumArr.push(parseInt(num.join('')));
        });
    }
    possibleNumArr = new Set([...possibleNumArr]);

    for (const num of possibleNumArr) {
        if (isPrime(num)) answer++;
    }
    return answer;
}

console.log(solution('011'));
