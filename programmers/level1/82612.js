function solution(price, money, count) {
    let sum = 0;

    for (let i = price; i <= price * count; i += price) {
        sum = sum + i;
    }

    return sum - money > 0 ? sum - money : 0;
}

console.log(solution(3, 20, 4));
