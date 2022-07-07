function solution(phoneNumber) {
    const numberArray = phoneNumber.split('');
    return numberArray
        .map((number, index) => {
            if (index >= numberArray.length - 4) return number;
            return '*';
        })
        .join('');
}

console.log(solution('027778888'));
