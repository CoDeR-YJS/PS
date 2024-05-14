x = [False] * 30 

for i in range(28):
  a = int(input())
  x[a-1] = True

for i in range(30):
  if x[i] == False:
    print(i+1)