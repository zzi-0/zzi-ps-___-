function solution(info, query) {
    var answer = [];
    let conditionList = [];
    for (const q of query) {
        const condition = q.split(' ');
        let a = [];
        for (const c of condition) {
            if (c !== '-' && c !== 'and') a.push(c);
        }
        conditionList.push(a);
    }

    for (const c of conditionList) {
        let count = 0;
        let a = info.map((i) =>
            c.every((x) => {
                if (isNaN(x)) {
                    return i.includes(x);
                } else {
                    return Number(x) <= i.split(' ')[4];
                }
            })
        );
        for (const result of a) {
            if (result) count++;
        }
        answer.push(count);
    }

    return answer;
}

console.log(
    solution(
        [
            'java backend junior pizza 150',
            'python frontend senior chicken 210',
            'python frontend senior chicken 150',
            'cpp backend senior pizza 260',
            'java backend junior chicken 80',
            'python backend senior chicken 50',
        ],
        [
            'java and backend and junior and pizza 100',
            'python and frontend and senior and chicken 200',
            'cpp and - and senior and pizza 250',
            '- and backend and senior and - 150',
            '- and - and - and chicken 100',
            '- and - and - and - 150',
        ]
    )
);
