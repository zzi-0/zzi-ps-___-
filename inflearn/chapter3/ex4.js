/*
- 가장 짧은 문자거리

한 개의 문자열 s와 문자 t가 주어지면 문자열 s의 각 문자가 문자 t와 떨어진 최소거리를 출 력하는 프로그램을 작성하세요.


▣ 입력설명
첫 번째 줄에 문자열 s와 문자 t가 주어진다. 문자열과 문자는 소문자로만 주어집니다. 문자열의 길이는 100을 넘지 않는다.

▣ 출력설명
첫 번째 줄에 각 문자열 s의 각 문자가 문자 t와 떨어진 거리를 순서대로 출력한다.


*/

const solution = (string) => {
  let result = [];
  let cnt = 100;
  for (let i = 0; i < string.length; i++) {
    if (string[i] !== "e") cnt++;
    else cnt = 0;
    result.push(cnt);
  }
  cnt = 100;
  for (let i = string.length; i >= 0; i--) {
    if (string[i] !== "e") cnt++;
    else cnt = 0;
    if (result[i] > cnt) result[i] = cnt;
  }
  return result;
};

console.log(solution("teachermode"));
