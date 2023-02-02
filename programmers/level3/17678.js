function solution(n, t, m, timetable) {
    let answer = '';
    const krews = []
    let count = 0
    let current_hour = 9
    let current_min = 0
    let queue = []

    timetable.forEach((time) => {
        [hour,min] = time.split(":")
        krews.push([parseInt(hour),parseInt(min)])
    })
    
    krews.sort((a,b) => {
        if (a[0] === b[0]) return a[1] - b[1]
        else return a[0] - b[0]
    })
    
    while(true) {
        let p = 0
        queue = []
        for (let i = 0; i < krews.length; i++) {
            const [hour,min] = krews[i];
            if (p >= m) {
                break;
            }
            if (current_hour > hour || (current_hour === hour && current_min >= min)) {
                queue.push([hour,min])
                krews.shift()
                i -= 1;
                p += 1
            } else {
                break;
            }
        }
        count += 1
        if (count == n) {
            if (queue.length < m) {
                current_hour = String(current_hour)
                current_min = String(current_min)
                if (current_hour.length === 1){
                    current_hour = 0 + current_hour
                } 
                if (current_min.length === 1){
                    current_min = 0 + current_min
                }
                answer = current_hour+":"+current_min
            } else {
                let [answer_hour,answer_min] = queue.pop()
                if (answer_min === 0) {
                    answer_hour -= 1
                    answer_min = 59
                } else {
                    answer_min -= 1
                }
                answer_hour = String(answer_hour)
                answer_min = String(answer_min)
                if (answer_hour.length === 1){
                    answer_hour = 0 + answer_hour
                } 
                if (answer_min.length === 1){
                    answer_min = 0 + answer_min
                }
                answer = answer_hour+":"+answer_min
            }
            break
        }
        current_min += t
        if (current_min >= 60) {
            current_hour += 1
            current_min = current_min % 60
        } 
    }
    return answer;
}

console.log(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
console.log(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
console.log(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
