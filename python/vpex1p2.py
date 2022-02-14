N = int(input())
nums = [int(a) for a in input().split()]
average = sum(nums) / len(nums)
c = 0
for n in nums:
	if n != average:
		c += 1
print(c)