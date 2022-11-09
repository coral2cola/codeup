h, b, c, s = map(int, input().split())

# 1초에 h번
# b bit만큼
# 채널개수 c
# 녹음 시간 s

# h*b*c*s /8/1024/1024

print(format(h*b*c*s/8/1024/1024, ".1f"), 'MB')