# 입력 처리
n = int(input())
scores = list(map(int, input().split()))

# 최댓값 찾기
max_score = max(scores)

# 점수 조작 및 새로운 평균 계산
new_scores = [(score / max_score) * 100 for score in scores]
new_average = sum(new_scores) / n

# 결과 출력
print(new_average)