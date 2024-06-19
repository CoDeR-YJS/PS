# 입력 받기
A = input().strip()
operator = input().strip()
B = input().strip()

# A와 B가 모두 10의 제곱 형태임을 가정
# 따라서 문자열로 받아서 바로 연산을 수행할 수 있습니다.

# 연산 수행
if operator == '+':
    result = int(A) + int(B)
elif operator == '*':
    result = int(A) * int(B)

# 결과 출력
print(result)
