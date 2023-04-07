import time


start_nums = [18,11,9,0,5,1]

def get_indices(item, in_list):
	return [i for i, v in enumerate(in_list) if v == item]

def add_to_dict(k, v, d):
	if k not in d:
		d[k] = [v]
	else:
		d[k] = last_nums_buffer(v, d[k])
		#d[k].append(v)
	return d

def last_nums_buffer(v, l):
	buffer_length = 5
	if len(l) >= buffer_length:
		l.pop(0)
	l.append(v)
	return l

def solution01(start_nums, turns):

	nums = []

	#run the game
	for i in range(turns):
		if i < len(start_nums):
			next_num = start_nums[i]
		else:
			last_num = nums[-1]
			nums_excluding_last_num = nums[:-1]
			if last_num not in nums_excluding_last_num:
				next_num = 0
			else:
				#had been said before
				indices = get_indices(last_num, nums_excluding_last_num)
				next_num = (i - 1) - indices[-1]

		nums.append(next_num)		
		#print(f"Turn {i + 1}:", next_num)


	print("—————")
	return nums[-1]

def solution02(start_nums, turns):

	nums = {} #for lookups
	last_nums = [] #for order
	last_num = "—"

	#run the game
	for i in range(turns):
		if i % 100000 == 0:
			print(i, f"{i/turns * 100}%")
		if i < len(start_nums):
			next_num = start_nums[i]
		else:
			last_num = last_nums[-1]
			if nums[last_num] == [i-1]: #maybe skip the "not in" part ? 
				next_num = 0
			else:
				#next_num = "—"
				#print("last_num", last_num, nums[last_num])
				next_num = (i - 1) - nums[last_num][-2]



		if next_num not in nums:
			nums[next_num] = [i]
		else:
			nums[next_num].append(i)


		last_nums.append(next_num)


	print("—————")
	#print(nums)
	return last_nums[-1]

solution01_start_time = time.time()
solution01_result = solution01(start_nums, 2020)
solution01_time = time.time() - solution01_start_time



solution02_start_time = time.time()
solution02_result = solution02(start_nums, 30000000) # 30000000
solution02_time = time.time() - solution02_start_time

print("Solution 01:", solution01_result, "in", solution01_time)
print("Solution 02:", solution02_result, "in", solution02_time)


