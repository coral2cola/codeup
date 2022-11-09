w, h, b = map(int, input().split())

# b는 bit
# 한 점 24 bit

print(format(w*h*b/8/1024/1024, ".2f"), 'MB')