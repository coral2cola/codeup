w, h, b = map(int, input().split())

# bė bit
# ķ ģ  24 bit

print(format(w*h*b/8/1024/1024, ".2f"), 'MB')