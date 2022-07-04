function solution(n, lost, reserve) {
    var answer = 0;
    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a - b);

    const filteredLost = lost.filter(function (item) {
        return !reserve.includes(item);
    });

    const filteredReserve = reserve.filter(function (item) {
        return !lost.includes(item);
    });

    for (let i = 0; i < filteredReserve.length; i++) {
        if (filteredLost.includes(filteredReserve[i] - 1)) {
            filteredReserve.splice(i, 1);
            i--;
            filteredLost.shift();
        } else if (filteredLost.includes(filteredReserve[i] + 1)) {
            filteredReserve.splice(i, 1);
            i--;
            filteredLost.shift();
        }
    }
    answer = n - filteredLost.length;
    return answer;
}
console.log(solution(5, [3], [3]));
