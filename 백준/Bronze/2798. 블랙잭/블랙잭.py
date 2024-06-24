N,M = map(int,input().split())

cards = list(map(int,input().split()))

max_sum = 0

for i in range(N):
   for j in range(i+1,N):
     for k in range(j+1,N):
       current_sum = cards[i] + cards[j] + cards[k]
       if current_sum <= M:
         if current_sum > max_sum:
           max_sum = current_sum

print(max_sum)