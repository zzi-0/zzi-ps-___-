/*
- 대문자 찾기

한 개의 문자열을 입력받아 해당 문자열에 알파벳 대문자가 몇 개 있는지 알아내는 프로그램 을 작성하세요.

▣ 입력설명
첫 줄에 문자열이 입력된다. 문자열의 길이는 100을 넘지 않습니다.

▣ 출력설명
첫 줄에 대문자의 개수를 출력한다.

*/

const solution = (str) => {
  let char = str.split("");
  char = char.filter((character) => {
    if (character.toLowerCase() !== character) return character;
  });
  return char.length;
};

console.log(solution("KoreaTimeGood"));
