function isPrime(num) {
    if (num === 1) return false;
    for (let i = 2; i < num; i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function solution(nums) {
    let check = Array.from({ length: nums.length }, () => 0);
    let primeStringList = [];
    let pickNums = [];

    function pick(L, sum) {
        if (L === 3) {
            if (isPrime(sum)) {
                const sortedPickNums = [...pickNums].sort(function (a, b) {
                    return a - b;
                });
                let primeString = '';
                for (const num of sortedPickNums) {
                    primeString += num;
                }
                if (!primeStringList.includes(primeString)) primeStringList.push(primeString);
            }
        } else {
            for (let i = 0; i < nums.length; i++) {
                if (check[i] === 0) {
                    check[i] = 1;
                    pickNums.push(nums[i]);
                    pick(L + 1, sum + nums[i]);
                    pickNums.pop();
                    check[i] = 0;
                }
            }
        }
    }

    pick(0, 0);

    return primeStringList.length;
}

console.log(solution([1, 2, 7, 6, 4]));
