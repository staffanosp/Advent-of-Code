import time

with open("input.txt","r") as f:
	in_data = [int(i.strip()) for i in f.readlines()]

PREAMBLE_LEN = 25

def print_progress(active_start = 0, active_length = 0, sleep = 0):
	resolution = 120

	#active_start = 0.4
	#active_length = 0.2

	segment01 = round(active_start * resolution)
	segment02 = round(active_length  * resolution) if round(active_length  * resolution) > 1 else 1
	segment03 = round(resolution - segment01 - segment02)

	output = ""
	for i in range(segment01):
		output += "."
	for i in range(segment02):
		output += "|"
	for i in range(segment03):
		output += "."

	output += f" — {round(active_start * 100, 1)} %"

	print(output, end = '\r')
	time.sleep(sleep)

def sums_of_list_items(in_list):
	return [a + b for b in in_list for a in in_list]

def find_contiguous_range(in_list, invalid_number):
	for i, a in enumerate(in_list):
		sum = 0
		range_data = []

		for i_b, b in enumerate(in_list[i:]):
			#print(i_b)
			sum += b
			range_data.append(b)


			print_progress(i / len(in_list), i_b / len(in_list), 0.00001)

			if sum == invalid_number:
				print()
				return max(range_data) + min(range_data)

			if sum > invalid_number:
				break
	
	return False



def solution01(in_data):
	for i, data in enumerate(in_data):
		if i > PREAMBLE_LEN - 1:
			if not data in sums_of_list_items(in_data[i - PREAMBLE_LEN:i]):
				return data
	return False



def solution02(in_data, invalid_number):
	return find_contiguous_range(in_data, invalid_number)




solution01_start_time = time.time()
print("Solution 01:", solution01(in_data), "in", time.time() - solution01_start_time)


solution02_start_time = time.time()
print("Solution 02:", solution02(in_data, solution01(in_data)), "in", time.time() - solution02_start_time)