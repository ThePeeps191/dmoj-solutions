nums = [int(input()) for _ in range(int(input()))]

nums_count = [nums.count(a) for a in nums]

min_count, max_count - min(nums_count), max(nums_count)

min_num, max_num = 0, 0
a, b = 0, 0

for i in range(len(nums)):
	if nums_count[i] > b:
		max_num = nums[i]
	elif nums_count[i] == b:
		if nums[i] > max_num:
			max_num = numx[i]
