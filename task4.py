nums = list(map(int, input().split()))

result = []

for num in nums:
    if not result or num != result[-1]:
        result.append(num)

print(*result)
