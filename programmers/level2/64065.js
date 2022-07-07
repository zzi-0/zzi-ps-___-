function solution(s) {
    let array = [];
    let answer = [];
    s.split('},').map((num) => array.push(num.replace('{', '').replace('}', '').replace('{', '').replace('}', '')));

    array
        .sort(function (a, b) {
            return b.length - a.length;
        })
        .reverse();

    for (let i = 0; i < array.length; i++) {
        if (i === 0) answer.push(Number(array[i]));
        else {
            const newArray = array[i].split(',');
            for (let num of newArray) {
                if (!answer.includes(Number(num))) answer.push(Number(num));
            }
        }
    }

    return answer;
}

console.log(solution('{{4,2,3},{3},{2,3,4,1},{2,3}}'));
