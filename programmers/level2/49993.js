// 15:50
function solution(skill, skillTrees) {
    let answer = skillTrees.length;

    for (const skillTree of skillTrees) {
        let tree = [];
        for (let i = 0; i < skillTree.length; i++) {
            if (skill.includes(skillTree[i])) tree.push(skillTree[i]);
        }
        let skillStr = tree.join('');

        for (let i = 0; i < skillStr.length; i++) {
            if (skill[i] !== skillStr[i]) {
                answer--;
                break;
            }
        }
    }

    return answer;
}

console.log(solution('CBD', ['CDE', 'CBADF', 'AECB', 'BDAC', 'EF']));
