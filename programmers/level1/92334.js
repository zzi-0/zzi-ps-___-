function solution(id_list, report, k) {
  const reports = [...new Set(report)];
  var answer = Array.from({ length: id_list.length }, () => 0);
  let bannedId = [];

  // 신고 받은 횟수를 넣은 map
  let counts = new Map();

  // 초기화
  for (let x of id_list) {
    counts.set(x, 0);
  }

  // 신고 받은 횟수 넣어주기
  for (let x of reports) {
    const arr = x.split(" ");
    const count = counts.get(arr[1]);
    counts.set(arr[1], count + 1);
  }

  // 정지당한 id 알아내기
  for (let [userId, value] of counts) {
    if (value >= k) bannedId.push(userId);
  }

  // 정지당한 id에게 이메일을 보냈던 사람에게 메일 보내기
  for (let i = 0; i < reports.length; i++) {
    const arr = reports[i].split(" ");
    if (bannedId.includes(arr[1])) {
      const index = id_list.indexOf(arr[0]);
      answer[index] = answer[index] + 1;
    }
  }

  return answer;
}

console.log(
  solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
);
