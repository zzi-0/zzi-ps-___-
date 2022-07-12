const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((el) => [fixed, ...el]);
        results.push(...attached);
    });

    return results; // 결과 담긴 results return
};

function solution(orders, courses) {
    var answer = [];
    let menuMap = new Map();
    orders.forEach((order) => {
        order = order.split('').sort().join('');
        courses.forEach((course) => {
            const combinations = getCombinations([...order], course);
            combinations.forEach((combination) => {
                const combi = combination.join('');
                if (!menuMap.has(combi)) menuMap.set(combi, 1);
                else menuMap.set(combi, menuMap.get(combi) + 1);
            });
        });
    });

    for (const course of courses) {
        let menuCountList = [];
        let maxCount = 0;
        for (const [menu, count] of menuMap) {
            if (menu.length === course) menuCountList.push(count);
        }
        maxCount = Math.max(...menuCountList);
        if (maxCount >= 2) {
            for (const [menu, count] of menuMap) {
                if (menu.length === course && count < maxCount) menuMap.delete(menu);
            }
        } else {
            for (const [menu, count] of menuMap) {
                if (menu.length === course) menuMap.delete(menu);
            }
        }
    }

    for (const [menu, count] of menuMap) {
        answer.push(menu);
    }
    return answer.sort();
}

console.log(solution(['XYZ', 'XWY', 'WXA'], [2, 3, 4]));
