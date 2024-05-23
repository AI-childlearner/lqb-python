import math

x1, y1 = map(float, input().split())
ans = 0

while True:
    try:
        x1, y1, x2, y2 = map(float, input().split())
        dx = x1 - x2
        dy = y1 - y2
        ans += math.sqrt(dx * dx + dy * dy) * 2
    except ValueError:
        break

minutes = round(ans / 1000 / 20 * 60)
hour = minutes // 60
minutes %= 60
print(f"{hour}:{minutes:02}")
