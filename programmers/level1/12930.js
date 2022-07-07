function solution(s) {
    let char = '';
    const string = s.split(' ');
    const wordList = [];
    for (const word of string) {
        char = '';
        for (let j = 0; j < word.length; j++) {
            if (j % 2 === 0) char += word[j].toUpperCase();
            else char += word[j].toLowerCase();
        }
        wordList.push(char);
    }
    return wordList.join(' ');
}

console.log(solution('try hello world'));
