def min_skill_level_difference(A, B, C, D):
    # 가능한 팀 구성과 각각의 스킬 레벨 차이를 계산합니다.
    diff1 = abs((A + B) - (C + D))
    diff2 = abs((A + C) - (B + D))
    diff3 = abs((A + D) - (B + C))
    
    # 세 가지 경우 중 최솟값을 반환합니다.
    return min(diff1, diff2, diff3)

# 입력을 받습니다.
A, B, C, D = map(int, input().split())

# 결과를 출력합니다.
print(min_skill_level_difference(A, B, C, D))
