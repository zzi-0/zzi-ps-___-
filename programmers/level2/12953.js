const gcd = (a, b) => {
    while (b > 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};

const lcm = (a, b) => {
    return (a * b) / gcd(a, b);
};

function solution(arr) {
    let answer = arr[0];

    for (let i = 1; i < arr.length; i++) {
        answer = lcm(answer, arr[i]);
    }
    lcm();
    return answer;
}

console.log(solution([2, 6, 8, 14]));
