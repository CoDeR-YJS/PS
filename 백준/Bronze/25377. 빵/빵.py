def min_time_to_get_bread(N, stores):
  min_time = float('inf')
  found = False

  for A,B in stores:
    if A <= B:
      found = True
      min_time = min(min_time, B)

  return min_time if found else -1

N = int(input())
stores = [ map(int,input().split()) for i in range(N)  ]

print(min_time_to_get_bread(N,stores))



