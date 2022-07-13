// 나중에 꼭 다시풀어보기
const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((el) => [fixed, ...el]);
        results.push(...attached);
    });

    return results;
};

const isEqual = (a, b) => a.length === b.length && a.every((v, i) => v === b[i]);

function solution(relations) {
    var answer = 0;
    const columnLength = relations[0].length;
    const columnIndexes = Array(columnLength)
        .fill(0)
        .map((_, i) => i);
    const columnSet = [];
    let s = 0;

    for (let i = columnLength; i > 0; i--) {
        columnSet.push(...getCombinations(columnIndexes, i));
    }

    while (columnSet.length) {
        s = columnSet.pop();
        if (relations.map((v) => s.map((i) => v[i])).some((v, i, a) => i !== a.findIndex((_v) => isEqual(_v, v))))
            continue;

        answer++;
        for (let i = 0; i < columnSet.length; i++) {
            if (s.every((v) => columnSet[i].includes(v))) columnSet.splice(i--, 1);
        }
    }

    return answer;
}

console.log(
    solution([
        ['100', 'ryan', 'music', '2'],
        ['200', 'apeach', 'math', '2'],
        ['300', 'tube', 'computer', '3'],
        ['400', 'con', 'computer', '4'],
        ['500', 'muzi', 'music', '3'],
        ['600', 'apeach', 'music', '2'],
    ])
);
