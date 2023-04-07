import time

with open("input.txt","r") as f:
	input_list = [int(i.strip()) for i in f.readlines()]

def solution01(input_list):
	increase_counter = 0 
	for i, _ in enumerate(input_list):
		if i == 0:
			continue

		if input_list[i] > input_list[i-1]:
			increase_counter += 1

	return increase_counter

def solution02(input_list):
	windows_size = 3
	cleaned_data = []

	for i, _ in enumerate(input_list):
		window = input_list[i:i+windows_size]

		if len(window) < windows_size:
			break

		cleaned_data.append(sum(window))

	increase_counter = 0
	for i, _ in enumerate(cleaned_data):
		if i == 0:
			continue

		if cleaned_data[i] > cleaned_data[i-1]:
			increase_counter += 1

	return increase_counter


solution01_start_time = time.time()
solution01 = solution01(input_list)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(input_list)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")

