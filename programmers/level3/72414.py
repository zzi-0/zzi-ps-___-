def solution(play_time, adv_time, logs):
    answer = ''
    answer_int = 0
    max = 0
    n = len(logs)
    [play_hour,play_min,play_sec] = play_time.split(':')
    [adv_hour,adv_min,adv_sec] = adv_time.split(':')
    play_time = int(play_hour) * 60 * 60 + int(play_min) * 60 + int(play_sec)
    adv_time = int(adv_hour) * 60 * 60 + int(adv_min) * 60 + int(adv_sec)
    original = []
    play_list = []
    
    original.append('00:00:00')
    play_list.append((0,adv_time))
    for i in range(n):
        [i_start_time,i_end_time] = logs[i].split("-")
        [i_start_hour,i_start_min,i_start_sec] = i_start_time.split(':')
        [i_end_hour,i_end_min,i_end_sec] = i_end_time.split(':')
        adv_start = int(i_start_hour) * 60 * 60 + int(i_start_min) * 60 + int(i_start_sec)
        adv_end = int(i_end_hour) * 60 * 60 + int(i_end_min) * 60 + int(i_end_sec)
        play_list.append((adv_start,adv_end))
        original.append(i_start_time)
    
    for j in range(len(play_list)):
        play_start,play_end = play_list[j]
        adv_end = play_start + adv_time
        sum = 0
        
        if adv_end > play_time:
            adv_end = play_time
        for another_play_start,another_play_end in play_list:

            if play_start > another_play_end:
                continue
            
            if adv_start >= another_play_start:
                if another_play_end >= adv_end:
                    sum += (adv_end - play_start)
                else:
                    sum += (another_play_end - play_start)
            else:
                if another_play_end >= adv_end:
                    sum += (adv_end - another_play_start)
                else:
                    sum += (another_play_end - another_play_start)

        if max < sum:
            max = sum
            answer_int = play_start
        elif max == sum:
            if answer_int > play_start:
                answer_int = play_start
                answer = original[j]
    
    
    return answer


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))