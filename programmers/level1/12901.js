function solution(a, b) {
    const dayList = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    const monthList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let daySum = 0;

    if (a !== 1) daySum = monthList.slice(0, a - 1).reduce((sum, month) => sum + month);
    daySum = daySum + b;

    return dayList[daySum % 7];
}

console.log(solution(5, 24));
