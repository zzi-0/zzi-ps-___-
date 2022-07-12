function solution(s) {
    var answer = 1;
    let beforeStr = '';

    let str = s.split('');
    while (answer) {
        for (let i = 0; i < str.length - 1; i++) {
            if (str[i] === str[i + 1]) {
                str.splice(i - 1, 2);
                i--;
                i--;
            }
        }
        if (str.length === 0) break;
        if (beforeStr.length === str.length) {
            answer = 0;
            break;
        }
        beforeStr = [...str];
    }

    return answer;
}
console.log(solution('dccddd'));
