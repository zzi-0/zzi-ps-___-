function solution(s, n) {
    let answer = '';
    let codeAt;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === ' ') answer += ' ';
        else {
            codeAt = s.charCodeAt([i]) + n;
            if ((s[i] === s[i].toUpperCase() && codeAt > 90) || (s[i] === s[i].toLowerCase() && codeAt > 122))
                codeAt = codeAt - 26;

            answer += String.fromCharCode([codeAt]);
        }
    }
    return answer;
}

console.log(solution('a B z', 4));
