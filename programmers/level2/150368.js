function getCombinations(n) {
  const sale = [10, 20, 30, 40];
  const combinations = [];

  function dfs(level,temp){
    if (level === n) {
      combinations.push([...temp]);
    } else {
      for (let i = 0; i< 4; i++){
        temp.push(sale[i]);
        dfs(level+1,temp)
        temp.pop();
      }
    }
  }

  dfs(0,[]);
  return combinations;
}

function solution(users, emoticons) {
  let answer = [];

  const combinations = getCombinations(emoticons.length);
  // user가 가지고 있는 percent 보다 emoticons의 할인율이 높으면 무조건 삼! userSum에 할인된 가격 더해주기
  // userSum이 users가 가지고 있는 price보다 높으면 이모티콘 플러스 가입하기(plus++) + userSum 0으로 하기
  // sum += userSum
  for (let i = 0; i < combinations.length; i++){
    // [10, 10, 10, 10]
    const sales = combinations[i];
    let plus = 0;
    let sum = 0;
    for (let j = 0; j < users.length; j++){
      const [percent, price] = users[j];
      let userSum = 0;
      for (let k = 0; k < emoticons.length; k++){
        if (percent <= sales[k]) {
          userSum += emoticons[k] * (1 - (sales[k] / 100))
        }
      }
      if (userSum >= price) {
        plus++;
        userSum = 0;
      } 
      sum += userSum;
    }
    answer.push([plus,sum])

  }

  answer.sort((a,b) => {
    if (a[0] - b[0]) {
      return b[0] - a[0]
    } else if (a[0] === b[0]){
      return b[1] - a[1];
    }
  })

  return answer[0];
}

console.log(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]));
// 최대 4^7*100 = 1,638,400 -> 완전탐색이 가능할 것 같다. 