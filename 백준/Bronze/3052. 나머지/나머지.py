ans = [0] * 42
for i in range(0,10):
  x = int(input())
  ans[x%42] = 1

total = 0 

for i in range(0,42) :
  total += ans[i]

print(total)