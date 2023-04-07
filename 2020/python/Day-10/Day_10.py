import time

with open("input.txt","r") as f:
	adaptors = [int(i.strip()) for i in f.readlines()]
	adaptors.sort()



def solution01(adaptors):
	
	chain = [0] + adaptors + [max(adaptors) + 3]

	#count differences
	diff1 = 0
	diff2 = 0
	diff3 = 0


	for i, val in enumerate(chain):
		if i > 0:
			if val - chain[i - 1] == 1:
				diff1 += 1
			elif val - chain[i - 1] == 2:
				diff2 += 1
			elif val - chain[i - 1] == 3:
				diff3 += 1
			else:
				return "ERROR!"

	return diff1 * diff3


def solution02(adaptors):

	adaptors = set(adaptors)
	cache = {}

	def count_ways(start, end):


		if start == end:
			return 1

		if start > end:
			return 0

		#check cache
		if start in cache:
			return cache[start]

		ways = 0

		for i in range(1,4):
			if start + i in adaptors:
				ways += count_ways(start + i, end)
		cache[start] = ways

		return ways

	return count_ways(0, max(adaptors))





solution01_start_time = time.time()
print("Solution 01:", solution01(adaptors), "in", time.time() - solution01_start_time)


solution02_start_time = time.time()
print("Solution 02:", solution02(adaptors), "in", time.time() - solution02_start_time)