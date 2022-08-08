const solution = (n) => {
    const dy = Array.from({ length: n + 1 });
    dy[1] = 1;
    dy[2] = 2;
    for (let i = 3; i <= n; i++) {
        dy[i] = (dy[i - 1] + dy[i - 2]) % 1234567;
    }
    return dy[n];
};

// 3칸 = 총 2칸 + 1칸 / 총 1칸 + 2칸
// 4칸 = 총 3칸 + 1칸 / 총 2칸 + 2칸

console.log(solution(5));
