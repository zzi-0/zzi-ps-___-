function solution(s) {
    let beforeStr = '';
    let stack = [];
    let minLength = 999;
    if (s.length === 1) return 1;
    for (let i = 1; i <= s.length / 2; i++) {
        let answer = '';
        for (let j = 0; j < s.length; j += i) {
            if (beforeStr === s.slice(j, i + j) || stack.length === 0) {
                stack.push(s.slice(j, i + j));
            } else {
                if (stack.length === 1) answer += stack.pop();
                else answer += stack.length + stack.pop();
                while (stack.length) stack.pop();
                stack.push(s.slice(j, i + j));
            }
            beforeStr = s.slice(j, i + j);
        }
        if (stack.length === 1) answer += stack.pop();
        else answer += stack.length + stack.pop();
        while (stack.length) stack.pop();

        if (minLength > answer.length) minLength = answer.length;
    }

    return minLength;
}
console.log(solution('a'));
