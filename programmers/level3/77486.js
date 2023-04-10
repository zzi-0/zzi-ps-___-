function solution(enroll, referral, seller, amount) {
  const answer = new Map();
  const parent = new Map();
  const result = [];
  for (let i = 0; i < enroll.length; i++) {
    parent.set(enroll[i], referral[i]);
    answer.set(enroll[i], 0);
  }

  for (let i = 0; i < seller.length; i++) {
    dfs(seller[i], amount[i] * 100);
  }

  function dfs(name, amount) {
    const a = Math.ceil(amount * 0.9);
    let p_amount = answer.get(name);
    p_amount += a;
    answer.set(name, p_amount);
    const p = parent.get(name);
    if (p === "-") return;
    if (amount - a) {
      dfs(p, amount - a);
    }
  }

  for (let [key, value] of answer) {
    result.push(value);
  }

  return result;
}

console.log(
  solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4]
  )
);
