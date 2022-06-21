/*
- 올바른 괄호

괄호가 입력되면 올바른 괄호이면 “YES", 올바르지 않으면 ”NO"를 출력합니다.
(())() 이것은 괄호의 쌍이 올바르게 위치하는 거지만, (()()))은 올바른 괄호가 아니다.

▣ 입력설명
첫 번째 줄에 괄호 문자열이 입력됩니다. 문자열의 최대 길이는 30이다.

▣ 출력설명
첫 번째 줄에 YES, NO를 출력한다.
*/

const solution = (str) => {
  let result = [];
  for (let x of str) {
    if (x === "(") result.push("(");
    else {
      if (result.length === 0) return "NO";
      else result.pop();
    }
  }
  return result.length === 0 ? "YES" : "NO";
};

console.log(solution("(()))("));
