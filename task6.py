n = input().strip()

if n[0] == '-':
    reversed_num = int(n[:0:-1])
    print(-reversed_num)
else:
    reversed_num = int(n[::-1])
    print(reversed_num)