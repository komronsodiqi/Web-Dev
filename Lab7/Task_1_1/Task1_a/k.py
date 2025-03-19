n = int(input())
h = (n // 60) % 24
m = n % 60
print ('%d %d' % (h, m))