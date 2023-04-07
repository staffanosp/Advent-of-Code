import time

with open("input.txt","r") as f:
	boarding_passes = [i.strip() for i in f.readlines()]

ROWS = 128
COLS = 8

def chars_to_int(chars, max_num):
	nums = [num for num in range(0,max_num)]

	for c in chars:
		if c == "F" or c == "L":
			lo = 0
			hi = int(len(nums) / 2)
		else:
			lo = int(len(nums) / 2)
			hi = len(nums)

		nums = [nums[i] for i in range(lo, hi)]

	return nums[0]

def boarding_pass_to_seatID(boarding_pass):
	row = chars_to_int(boarding_pass[:7], ROWS)
	col = chars_to_int(boarding_pass[7:], COLS)
	return row * 8 + col


def solution01(boarding_passes):
	return max([boarding_pass_to_seatID(boarding_pass) for boarding_pass in boarding_passes])


def solution02(boarding_passes):
	seatIDs = [boarding_pass_to_seatID(boarding_pass) for boarding_pass in boarding_passes]
	seatIDs.sort()

	#loop to find gap in list
	for i, expected_id in enumerate(range(seatIDs[0], seatIDs[-1])):
		if expected_id != seatIDs[i]:
			return expected_id


solution01_start_time = time.time()
solution01 = solution01(boarding_passes)
solution01_total_time = time.time() - solution01_start_time

solution02_start_time = time.time()
solution02 = solution02(boarding_passes)
solution02_total_time = time.time() - solution02_start_time

print("Solution 01:", solution01, "in", solution01_total_time)
print("Solution 02:", solution02, "in", solution02_total_time)
