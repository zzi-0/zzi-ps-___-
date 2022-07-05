function solution(answers) {
    const student1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5];
    const student2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5];
    const student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    let student1Count = 0;
    let student2Count = 0;
    let student3Count = 0;
    let result = [];
    let answer = [];

    answers.map((answer, index) => {
        let student1Index = index >= student1.length ? index % student1.length : index;
        let student2Index = index >= student2.length ? index % student2.length : index;
        let student3Index = index >= student3.length ? index % student3.length : index;

        if (answer === student1[student1Index]) student1Count++;
        if (answer === student2[student2Index]) student2Count++;
        if (answer === student3[student3Index]) student3Count++;
    });

    result.push(student1Count);
    result.push(student2Count);
    result.push(student3Count);

    result.map((count, index) => {
        if (count === Math.max(...result)) answer.push(index + 1);
    });

    return answer.sort((a, b) => a - b);
}

console.log(solution([1, 2, 3, 4, 5]));
