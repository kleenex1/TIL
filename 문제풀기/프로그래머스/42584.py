from collections import deque

def solution(prices):
    answer = []
    
    dq = deque(prices)
    
    while dq:
        cnt = 0
        price = dq.popleft()
        for i in dq:
            cnt += 1
            if price > i:
                break
        answer.append(cnt)
    return answer