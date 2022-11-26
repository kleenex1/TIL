progresses = [93,30,55]
speeds = [1,30,5]

def solution(progresses, speeds):
    answer = []
    
    count = 0
    time = 0

    while len(progresses):
        if progresses[0] + time*speeds[0] > 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0 :
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

print(solution(progresses, speeds))