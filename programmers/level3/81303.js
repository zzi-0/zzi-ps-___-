/* eslint-disable no-case-declarations */
const Node = function (index, prevNode) {
  this.index = index;
  this.prev = prevNode;
  this.next = null;
};

function solution(n, k, cmd) {
  let answer = Array(n).fill("O");
  let root = new Node(0);
  let currentNode = root;
  let prevNode = root;

  for (let i = 1; i < n; i++) {
    const newNode = new Node(i, prevNode);
    prevNode.next = newNode;
    prevNode = newNode;

    if (i === k) {
      currentNode = newNode;
    }
  }

  const deletedList = [];
  for (const c of cmd) {
    const [command, number] = c.split(" ");
    let i = 0;
    switch (command) {
      case "D":
        while (i < number && currentNode.next) {
          currentNode = currentNode.next;
          i++;
        }
        break;
      case "U":
        while (i < number && currentNode.prev) {
          currentNode = currentNode.prev;
          i++;
        }
        break;
      case "C":
        deletedList.push(currentNode);
        const prevNode = currentNode.prev;
        const nextNode = currentNode.next;
        if (prevNode && nextNode) {
          prevNode.next = nextNode;
          nextNode.prev = prevNode;
          currentNode = nextNode;
        } else if (prevNode) {
          prevNode.next = null;
          currentNode = prevNode;
        } else if (nextNode) {
          nextNode.prev = null;
          currentNode = nextNode;
        }
        break;
      case "Z":
        const recentNode = deletedList.pop();
        const recentPrevNode = recentNode.prev;
        const recentNextNode = recentNode.next;
        if (recentPrevNode) {
          recentPrevNode.next = recentNode;
        }
        if (recentNextNode) {
          recentNextNode.prev = recentNode;
        }
        break;
    }
  }
  deletedList.map((node) => {
    answer[node.index] = "X";
  });
  return answer.join("");
}

console.log(
  solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
);
