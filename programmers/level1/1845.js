function solution(nums) {
    return Math.min([...new Set(nums)].length, nums.length / 2);
}

console.log(solution([3, 1, 2, 3]));
