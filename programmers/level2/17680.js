function solution(cacheSize, cities) {
    let answer = 0;
    let stack = [];
    if (cacheSize === 0) return cities.length * 5;
    for (let i = 0; i < cities.length; i++) {
        cities[i] = cities[i].toUpperCase();

        if (stack.includes(cities[i])) {
            stack.splice(stack.indexOf(cities[i]), 1);
            stack.push(cities[i]);
            answer++;
            continue;
        }

        // 스택에 해당하는 도시가 없을 경우

        // 아직 스택에 들어갈 공간 있음
        if (stack.length >= cacheSize) stack.shift();
        stack.push(cities[i]);
        answer += 5;
    }
    return answer;
}

console.log(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'LA', 'LA']));
