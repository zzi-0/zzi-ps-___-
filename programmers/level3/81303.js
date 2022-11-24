function solution(n, k, cmd) {
  let answer = "";
  let pointer = k;
  let table = Array.from({ length: n }, (v, i) => i).map((index) => {
    return {
      original: index,
    };
  });
  const deletedList = [];
  let j = 0;

  for (let i = 0; i < cmd.length; i++) {
    const [command, number] = cmd[i].split(" ");
    if (command === "U") {
      pointer -= Number(number);
    }
    if (command === "D") {
      pointer += Number(number);
    }
    if (command === "C") {
      const len = table.length;
      const deletedItem = table.splice(pointer, 1);
      deletedList.push(...deletedItem);
      if (pointer === len - 1) {
        pointer -= 1;
      }
    }
    if (command === "Z") {
      const recentItem = deletedList.pop();
      if (recentItem.original <= pointer) {
        pointer++;
      }
      table.push(recentItem);
      table.sort((a, b) => a.original - b.original);
    }
  }

  for (let i = 0; i < n; i++) {
    if (j > table.length - 1) {
      answer += "X";
    } else if (table[j].original === i) {
      answer += "O";
      j++;
    } else {
      answer += "X";
    }
  }

  return answer;
}

console.log(
  solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
);
