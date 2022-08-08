function solution(s) {
    var answer = '';
    const array = s.toLowerCase().split(' ');
    for (const string of array) {
        for (let i = 0; i < string.length; i++) {
            if (i === 0) answer += string[i].toUpperCase();
            else answer += string[i].toLowerCase();
        }
        answer += ' ';
    }
    return answer.substr(0, s.length);
}
console.log(solution('3people unFollowed me'));
