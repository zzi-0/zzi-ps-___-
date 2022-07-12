function solution(record) {
    let answer = [];
    let userMap = new Map();

    let user = record.map((info) => {
        const [action, uid, nickName] = info.split(' ');
        return {
            action,
            uid,
            nickName,
        };
    });

    user.map((userInfo) => {
        if (!userMap.has(userInfo.uid) || userInfo.action === 'Change' || userInfo.action === 'Enter') {
            userMap.set(userInfo.uid, userInfo.nickName);
        }
    });

    record.map((info) => {
        const [action, uid, nickName] = info.split(' ');
        const changeName = userMap.get(uid);
        if (action === 'Enter') answer.push(`${changeName}님이 들어왔습니다.`);
        else if (action === 'Leave') answer.push(`${changeName}님이 나갔습니다.`);
    });

    return answer;
}

console.log(
    solution([
        'Enter uid1234 Muzi',
        'Enter uid4567 Prodo',
        'Leave uid1234',
        'Enter uid1234 Prodo',
        'Change uid4567 Ryan',
    ])
);
