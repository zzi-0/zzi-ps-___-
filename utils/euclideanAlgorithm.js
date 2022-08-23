// 최대 공약수
const gcd = (a, b) => {
    while (b > 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};

// 최소 공배수
const lcm = (a, b) => {
    return (a * b) / gcd(a, b);
};
