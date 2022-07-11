function solution(number, k) {
    let stack = [];

    for (let i = 0; i < number.length; i++) {
        while (k > 0 && stack[stack.length - 1] < number[i]) {
            stack.pop();
            k--;
        }
        stack.push(number[i]);
    }

    return stack.join('').slice(0, number.length - k);
}

console.log(solution('777', 1));
