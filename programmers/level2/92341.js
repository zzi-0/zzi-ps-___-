//14:40

const getMin = (startTime, endTime) => {
    const start = new Date('2022', '07', '15', startTime.split(':')[0], startTime.split(':')[1]);
    const end = new Date('2022', '07', '15', endTime.split(':')[0], endTime.split(':')[1]);
    const elapsedMSec = end.getTime() - start.getTime();
    return elapsedMSec / 1000 / 60;
};

function solution(fees, records) {
    const [baseTime, baseFee, unitTime, unitFee] = fees;
    let answer = [];
    let map = new Map();

    for (let i = 0; i < records.length; i++) {
        const [time, id, state] = records[i].split(' ');
        map.set(id, 0);
    }

    const mapToArray = [...map];
    map = new Map(mapToArray.sort((a, b) => a[0] - b[0]));

    map.forEach((value, key, mapObject) => {
        let arr = [];
        for (const record of records) {
            const [time, id, state] = record.split(' ');
            if (id === key) {
                if (state === 'IN') arr.push(time);
                else map.set(id, map.get(id) + getMin(arr.pop(), time));
            }
        }
        if (arr.length > 0) map.set(key, map.get(key) + getMin(arr.pop(), '23:59'));
    });

    map.forEach((value, key) => {
        if (value <= baseTime) answer.push(baseFee);
        else {
            const fee = baseFee + Math.ceil((value - baseTime) / unitTime) * unitFee;
            answer.push(fee);
        }
    });
    return answer;
}

console.log(
    solution(
        [180, 5000, 10, 600],
        [
            '05:34 5961 IN',
            '06:00 0000 IN',
            '06:34 0000 OUT',
            '07:59 5961 OUT',
            '07:59 0148 IN',
            '18:59 0000 IN',
            '19:09 0148 OUT',
            '22:59 5961 IN',
            '23:00 5961 OUT',
        ]
    )
);
