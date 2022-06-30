//https://programmers.co.kr/learn/courses/30/lessons/12912
function solution(a, b) {
  let bigNum = a;
  let smallNum = b;
  let answer = 0;

  if (a < b) {
    bigNum = b;
    smallNum = a;
  }
  if (a === b) answer = a;
  else {
    for (let i = smallNum; i <= bigNum; i++) {
      answer = answer + i;
    }
  }

  return answer;
}
