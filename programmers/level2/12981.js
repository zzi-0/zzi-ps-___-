// 11:25 -
function solution(n, words) {
    let answer = [0, 0];
    const wordList = [];

    // 한번 말하면 배열에 넣도록 , 말할때 배열에 같은게 있는지 확인 && 맞게 말했는지 확인
    // 배열 길이 % n = [나머지 + 1,몫 + 1]

    for (const word of words) {
        if (wordList.length === 0) wordList.push(word);
        else if (wordList.includes(word)) return [(wordList.length % n) + 1, Math.floor(wordList.length / n) + 1];
        else {
            const endWord = wordList[wordList.length - 1];
            const endAlphabet = endWord.split('').pop();
            const firstAlphabet = word.split('').shift();
            if (endAlphabet === firstAlphabet) wordList.push(word);
            else return [(wordList.length % n) + 1, Math.floor(wordList.length / n) + 1];
        }
    }

    return answer;
}

console.log(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']));
