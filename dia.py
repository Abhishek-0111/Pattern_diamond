n = int(input('dimen ?\n'))
tmp = n
c = 0
while tmp:
    c += 1
    tmp //= 10
for i in range(n):
    print()
    count = 1
    for j in range((n//2)+1):
        if j <= i < (n // 2 + 1):
            print("{0:{1}d}".format(count, c), end=' ')
            count += 1
        elif j <= n-i-1 and i >= (n//2 + 1):
            print("{0:{1}d}".format(count, c), end=' ')
            count += 1
