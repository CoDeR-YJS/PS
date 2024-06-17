def can_distribute_evenly(test_cases):
    results = []
    for case in test_cases:
        N = case[0]
        candies = case[1:]
        total_candies = sum(candies)
        if total_candies % N == 0:
            results.append("YES")
        else:
            results.append("NO")
    return results

# 입력 처리
import sys
input = sys.stdin.read
data = input().strip().split('\n')

T = int(data[0].strip())
test_cases = []
i = 1

for _ in range(T):
    while data[i].strip() == "":
        i += 1
    N = int(data[i].strip())
    i += 1
    candies = []
    for _ in range(N):
        candies.append(int(data[i].strip()))
        i += 1
    test_cases.append([N] + candies)

# 결과 계산 및 출력
results = can_distribute_evenly(test_cases)
for result in results:
    print(result)
