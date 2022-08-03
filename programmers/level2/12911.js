const getOneCount = (n) => {
    let oneCount = 0;
    let binary = n.toString(2);
    for (let i = 0; i < binary.length; i++) {
        if (binary[i] === '1') oneCount++;
    }

    return oneCount;
};

function solution(n) {
    let answer = 0;
    let oneCount = getOneCount(n);
    let i = n + 1;
    while (n) {
        if (oneCount === getOneCount(i)) {
            answer = i;
            break;
        }
        i++;
    }
    return answer;
}

console.log(solution(78));
