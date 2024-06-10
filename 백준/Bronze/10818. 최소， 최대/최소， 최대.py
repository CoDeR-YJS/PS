def find_min_max(n, numbers):
  min_value = numbers[0]
  max_value = numbers[0]

  for num in numbers[1:]:
    if num < min_value:
      min_value = num
    if num > max_value:
      max_value = num
  
  return min_value, max_value
  
n = int(input())
numbers = list(map(int, input().split()))

min_value, max_value = find_min_max(n, numbers)

print(min_value, max_value)
