/*
- 쇠막대기

후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 12입니다.

▣ 입력설명
한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

▣ 출력설명
잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.
*/

const solution = (str) => {
  let stack = [];
  let count = 0;
  for (let x = 0; x < str.length; x++) {
    if (str[x] === "(") stack.push(str[x]);
    else {
      stack.pop();
      if (str[x - 1] === "(") {
        count += stack.length;
      } else count += 1;
    }
  }
  return count;
};

console.log(solution("()(((()())(())()))(())"));
