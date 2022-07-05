function getRank(matchingCount) {
    if (matchingCount < 1) return 6;
    else return 7 - matchingCount;
}

function solution(lottos, winNums) {
    let answer = [];
    let matchingNumCount = 0;
    const filteredLottos = lottos.filter((lotto) => lotto !== 0);
    const unKnownNumCount = lottos.length - filteredLottos.length;

    for (const lotto of filteredLottos) {
        if (winNums.includes(lotto)) matchingNumCount++;
    }

    answer.push(getRank(matchingNumCount + unKnownNumCount));
    answer.push(getRank(matchingNumCount));
    return answer;
}

console.log(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]));
