function solution(str1, str2) {
    const engReg = /^[A-Z]*$/;
    let word1 = str1.toUpperCase();
    let word2 = str2.toUpperCase();

    let word1Set = [];
    let word2Set = [];
    let intersection = 0;

    for (let i = 0; i < word1.length - 1; i++) {
        if (engReg.test(word1[i] + word1[i + 1])) word1Set.push(word1[i] + word1[i + 1]);
    }
    for (let i = 0; i < word2.length - 1; i++) {
        if (engReg.test(word2[i] + word2[i + 1])) word2Set.push(word2[i] + word2[i + 1]);
    }

    // 교집합
    let check = Array.from({ length: word1Set.length }, () => 0);
    let check2 = Array.from({ length: word2Set.length }, () => 0);
    for (let i = 0; i < word1Set.length; i++) {
        for (let j = 0; j < word2Set.length; j++) {
            if (word1Set[i] === word2Set[j] && check[i] !== 1 && check2[j] !== 1) {
                intersection++;
                check[i] = 1;
                check2[j] = 1;
            }
        }
    }

    // 합집합
    for (const word of word1Set) {
        word2Set.push(word);
    }

    const numerator = intersection;
    const denominator = word2Set.length - intersection;

    return numerator === 0 || denominator === 0 ? 65536 : Math.floor((numerator / denominator) * 65536);
}

console.log(solution('A+C', 'DEF'));
