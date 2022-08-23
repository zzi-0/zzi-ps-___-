function solution(str) {
    let answer = true;
    let stack = [];

    str.split('').forEach((s) => {
        if (s === '(') stack.push('(');
        else {
            if (stack.pop() !== '(') return (answer = false);
        }
    });
    if (stack.length > 0) answer = false;
    return answer;
}

console.log(solution('(()('));
