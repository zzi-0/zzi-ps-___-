/*
- 공주 구하기

▣ 입력설명
첫 줄에 자연수 N(5<=N<=1,000)과 K(2<=K<=9)가 주어진다.

▣ 출력설명
첫 줄에 마지막 남은 왕자의 번호를 출력합니다.

*/

const solution = (n, k) => {
  let result;
  let queue = Array.from({ length: n }, (v, i) => i + 1);

  while (queue.length) {
    for (let i = 0; i < k - 1; i++) queue.push(queue.shift());
    queue.shift();
    if (queue.length === 1) result = queue.shift();
  }

  return result;
};

console.log(solution(8, 3));
