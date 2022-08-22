# 그냥 풀면 계속 시간초과 남. 에라토스테네스의 체라는 알고리즘 배우기!!


# 풀이과정
# 단순히 소인수 분해를 할 경우 시간 초과 발생, 최대 값인 10 
# 7
#  을 고려해야한다.
# 소수를 구해 소수로 나누고 더 이상 나눠질 수 없는 소수인지 판별하는 과정으로 연산횟수 줄이기

# 10 
# 7
#  의 제곱근까지의 소수를 구한다.
# 제곱근 이상의 수 중 소수로 더 이상 나눌 수 없으면 해당 수 역시 소수다.

# 소수를 구하기 위해 에라토스테네스의 체 알고리즘 사용

# 이미 제곱수인 경우 결과는 1
# 제곱수가 아닌 경우 동일한 소수로 나누는 횟수가 홀수인 경우 해당 소수를 곱하면 제곱 수가 된다.

# 소스코드
# T = int(input())

# 소수 구하기
max_n = int((10 ** 7) ** 0.5)
array = [True for _ in range(max_n + 1)]

for i in range(2, int(max_n ** 0.5) + 1):
    if array[i]:
        j = 2
        while i * j <= max_n:
            array[i * j] = False
            j += 1

prime = []

for i in range(2, len(array)):
    if array[i]:
        prime.append(i)

result = []

for t in range(1, T + 1):
    n = int(input())
    answer = 1

    if n ** 0.5 != int(n ** 0.5):
        for p in prime:
            count = 0
            while n % p == 0:
                n //= p
                count += 1
            if count % 2 != 0:
                answer *= p
            if n == 1 or p > n:
                break
        if n > 1:
            answer *= n

    result.append(answer)

for t in range(1, T + 1):
    print("#{} {}".format(t, result[t - 1]))