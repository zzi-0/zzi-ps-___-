/*
- 가운데 문자 출력

소문자로 된 단어(문자열)가 입력되면 그 단어의 가운데 문자를 출력하는 프로그램을 작성하세 요. 단 단어의 길이가 짝수일 경우 가운데 2개의 문자를 출력합니다.

▣ 입력설명
첫 줄에 문자열이 입력된다. 문자열의 길이는 100을 넘지 않습니다.

▣ 출력설명
첫 줄에 가운데 문자를 출력합니다.

*/

const solution = (str) => {
  if (str.length % 2 === 1) {
    return str[Math.ceil(str.length / 2) - 1];
  } else {
    return str[str.length / 2 - 1] + str[str.length / 2];
  }
};

console.log(solution("good"));
