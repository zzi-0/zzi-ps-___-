function solution(progresses, speeds) {
    var answer = [];
    let maxRemainDay = Math.ceil((100 - progresses[0]) / speeds[0]);
    let count = 0;

    const remainDays = progresses.map((progress, index) => {
        return Math.ceil((100 - progress) / speeds[index]);
    });

    remainDays.forEach((day, index) => {
        if (day <= maxRemainDay) {
            count++;
        } else {
            answer.push(count);
            maxRemainDay = day;
            count = 1;
        }
        if (index === remainDays.length - 1) answer.push(count);
    });

    return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]));
