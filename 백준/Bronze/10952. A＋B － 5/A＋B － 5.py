import sys
input = sys.stdin.readline

def main():
  while True : 
    x,y = input().strip().split()
    x = int(x)
    y = int(y)
    if x == 0 and y == 0 : 
      return 
    print(x+y)


main()
    

