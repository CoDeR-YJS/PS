def calculate_black_area(paper_positions):
  canvas = [[0] * 100 for _ in range(100)]

  for x,y in paper_positions:
    for i in range(x, x + 10):
      for j in range(y, y + 10):
        canvas[i][j] = 1

  black_area = 0
  for i in range(100) :
    black_area += sum(canvas[i])

  return black_area

n = int(input())
paper_positions = [] 

for i in range(n):
  paper_positions.append(list(map(int,input().split())))
  
black_area = calculate_black_area(paper_positions)
print(black_area)