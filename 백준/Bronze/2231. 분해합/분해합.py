def dp_sum(M):
  total = M
  while M > 0:
    total += M % 10 
    M //= 10

  return total 

N = int(input())
sign = True 
for M in range(1,N):
  if dp_sum(M) == N:
    print(M)
    sign = False 
    break

if (sign) : 
  print(0) 
    
