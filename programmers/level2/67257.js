const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);
    arr.forEach((fixed, index, origin) => {
        const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
        const permutations = getPermutations(rest, selectNumber - 1);
        const attached = permutations.map((el) => [fixed, ...el]);
        results.push(...attached);
    });

    return results;
};

function solution(expression) {
    let answer = 0;
    let operands = [];
    let operandsPriority = [];
    let separateExpression = [];
    let number = '';
    for (let i = 0; i < expression.length; i++) {
        if (expression[i] === '-' || expression[i] === '+' || expression[i] === '*') {
            if (separateExpression) {
                separateExpression.push(number);
                number = '';
            }
            operands.push(expression[i]);
            separateExpression.push(expression[i]);
        } else {
            number += expression[i];
        }
        if (i === expression.length - 1) separateExpression.push(number);
    }

    operands = [...new Set(operands)];
    operandsPriority = getPermutations(operands, operands.length);

    for (const operands of operandsPriority) {
        let realExpression = [...separateExpression];
        // console.log(operands);
        for (const operand of operands) {
            while (realExpression.length) {
                if (realExpression.indexOf(operand) === -1) break;
                let beforeOperand = realExpression.indexOf(operand) - 1;
                let afterOperand = realExpression.indexOf(operand) + 1;
                if (operand === '-') {
                    realExpression[beforeOperand] =
                        parseInt(realExpression[beforeOperand]) - parseInt(realExpression[afterOperand]);
                    realExpression.splice(beforeOperand + 1, 2);
                }
                if (operand === '+') {
                    realExpression[beforeOperand] =
                        parseInt(realExpression[beforeOperand]) + parseInt(realExpression[afterOperand]);
                    realExpression.splice(beforeOperand + 1, 2);
                }
                if (operand === '*') {
                    realExpression[beforeOperand] =
                        parseInt(realExpression[beforeOperand]) * parseInt(realExpression[afterOperand]);
                    realExpression.splice(beforeOperand + 1, 2);
                }
            }
        }
        if (answer < Math.abs(realExpression)) answer = Math.abs(realExpression);
    }
    return answer;
}

console.log(solution('50*6-3*2'));
