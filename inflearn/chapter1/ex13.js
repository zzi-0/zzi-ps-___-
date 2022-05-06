/*
- 대소문자 변환

대문자와 소문자가 같이 존재하는 문자열을 입력받아 대문자는 소문자로 소문자는 대문자로 변환하여 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 줄에 문자열이 입력된다. 문자열의 길이는 100을 넘지 않습니다.

▣ 출력설명
첫 줄에 대문자는 소문자로, 소문자는 대문자로 변환된 문자열을 출력합니다.

*/

const solution = (str) => {
  let char = str.split("");
  let newChar = [];
  char.map((character) => {
    // 소문자일 때
    if (character.toLowerCase() === character) {
      newChar.push(character.toUpperCase());
    }
    // 대문자일 때
    if (character.toUpperCase() === character) {
      newChar.push(character.toLowerCase());
    }
  });
  return newChar.join("");
};

console.log(solution("StuDY"));
