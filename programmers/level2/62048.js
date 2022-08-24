const gcd = (a, b) => {
    while (b > 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};

// 대각선이 지나는 사각형의 개수 : W + H - (W, H의 최대 공약수)
const solution = (w, h) => {
    const gcdValue = gcd(w, h);
    return w * h - (w + h - gcdValue);
};

console.log(solution(8, 12));
