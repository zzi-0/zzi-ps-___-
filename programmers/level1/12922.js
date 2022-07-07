function solution(n) {
  let answer = "";
  for (let i = 0; i < n / 2; i++) {
    answer += "수박";
  }
  return n % 2 === 0 ? answer : answer.split("").slice(0, n).join("");
}
console.log(solution(1));
