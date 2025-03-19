# 1 - solution
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

print((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1)

# 2 - solution
s = 3600 * int(input())
s += 60 * int(input())
s += int(input())

s -= 3600 * int(input())
s -= 60 * int(input())
s -= int(input())

print((-1) * s)