const isCorrectBracket = (string) => {
    let answer = true;
    const stack = [];
    for (let i = 0; i < string.length; i++) {
        if (string[i] === '[' || string[i] === '(' || string[i] === '{') stack.push(string[i]);
        else {
            const poppedString = stack.pop();
            if (!poppedString) {
                answer = false;
                break;
            }
            if (
                !(
                    (string[i] === ']' && poppedString === '[') ||
                    (string[i] === '}' && poppedString === '{') ||
                    (string[i] === ')' && poppedString === '(')
                )
            ) {
                answer = false;
                break;
            }
        }
    }
    if (stack.length > 0) answer = false;
    return answer;
};

const solution = (s) => {
    let answer = 0;
    let string = s;
    let i = 0;

    while (string) {
        const splitString = string.split('');
        const firstString = splitString.shift();
        splitString.push(firstString);
        string = splitString.join('');

        if (isCorrectBracket(string)) answer++;

        i++;
        if (i === s.length) break;
    }

    return answer;
};

console.log(solution('{{'));
