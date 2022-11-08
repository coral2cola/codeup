n = int(input())
result = 1
while True:
    n -= result
    if n <= 0:
        print(result)
        break
    
    result += 1