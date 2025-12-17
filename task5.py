nums = list(map(int, input().split()))
target = int(input())

seen = set()
found = False

for num in nums:
    needed = target - num
    if needed in seen:
        print([needed, num])
        found = True
        break
    seen.add(num)

if not found:
    print([])