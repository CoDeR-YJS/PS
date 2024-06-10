N,M = map(int,input().split())
A = [] 
B = [] 
for i in range(N): 
  row = list(map(int,input().split()))
  A.append(row)

for a in range(N):
  row = list(map(int,input().split()))
  B.append(row)

ans = [] 
for i in range(N):
  C = []
  for j in range(M):
    C.append(A[i][j] + B[i][j])
  ans.append(C)

for i in range(N): 
  for j in range(M) : 
    print(ans[i][j], end = " ")
  print()