function solution(msg) {
    let map = new Map();
    map.set('A', 1)
        .set('B', 2)
        .set('C', 3)
        .set('D', 4)
        .set('E', 5)
        .set('F', 6)
        .set('G', 7)
        .set('H', 8)
        .set('I', 9)
        .set('J', 10)
        .set('K', 11)
        .set('L', 12)
        .set('M', 13)
        .set('N', 14)
        .set('O', 15)
        .set('P', 16)
        .set('Q', 17)
        .set('R', 18)
        .set('S', 19)
        .set('T', 20)
        .set('U', 21)
        .set('V', 22)
        .set('W', 23)
        .set('X', 24)
        .set('Y', 25)
        .set('Z', 26);
    //console.log(map);
    var answer = [];
    for (let i = 0; i < msg.length; i++) {
        if (i < Math.ceil(msg.length / 2))
            for (let j = i + 1; j > 0; j--) {
                const s = msg.slice(i, i + j);
                const next = msg.slice(i + j, i + j + 1);
                // 해당 단어가 map에 있음
                if (map.has(s)) {
                    answer.push(map.get(s));
                    // 다음 단어 map에 저장
                    if (next) map.set(s + next, map.size + 1);
                    i += j - 1;
                    break;
                }
            }
        else
            for (let j = msg.length - i; j > 0; j--) {
                const s = msg.slice(i, i + j);
                const next = msg.slice(i + j, i + j + 1);
                //console.log(msg, s, next);
                // 해당 단어가 map에 있음
                if (map.has(s)) {
                    answer.push(map.get(s));
                    // 다음 단어 map에 저장
                    if (next) map.set(s + next, map.size + 1);
                    i += j - 1;
                    break;
                }
            }
    }
    //console.log(map);
    return answer;
}

console.log(solution('TOBEORNOTTOBEORTOBEORNOT'));
