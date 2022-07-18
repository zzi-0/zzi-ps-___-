const solution = (info, query) => {
    let answer = [];
    const map = {};

    const combination = (cnt, key, arr, score) => {
        if (cnt === 4) {
            if (!map[key]) map[key] = [score];
            else map[key].push(score);
            return;
        }
        combination(cnt + 1, key + arr[cnt], arr, score);
        combination(cnt + 1, key + '-', arr, score);
    };

    for (const i of info) {
        const arr = i.split(' ');
        const score = Number(arr.pop());
        combination(0, '', arr, score);
    }

    for (const key in map) {
        map[key].sort((a, b) => a - b);
    }

    for (let i = 0; i < query.length; i++) {
        const arr = query[i].replace(/ and /g, ' ').split(' ');
        const score = Number(arr.pop());
        const key = arr.join('');
        const scoreArray = map[key];

        if (scoreArray) {
            let left = 0;
            let right = scoreArray.length;
            while (left < right) {
                const mid = parseInt((left + right) / 2);
                if (scoreArray[mid] >= score) {
                    right = mid;
                } else if (scoreArray[mid] < score) {
                    left = mid + 1;
                }
            }
            answer.push(scoreArray.length - left);
        } else {
            answer.push(0);
        }
    }
    return answer;
};

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
