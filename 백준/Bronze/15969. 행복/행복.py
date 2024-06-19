N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
min_score = min(scores)

scores_difference = max_score - min_score

print(scores_difference)