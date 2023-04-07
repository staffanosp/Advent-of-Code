import time

with open("input.txt","r") as f:
	input_list = [i.strip() for i in f.readlines()]

def slope_check(input_list, right_step, down_step = 1):
	trees_counter = 0
	tree = "#"

	print("Right steps:", right_step)
	print("Down steps:", down_step)

	for i, line in enumerate(input_list):
		current_position = round(i / down_step) * right_step % len(line)
		current_char = line[current_position]
		
		if i % down_step == 0:
			print(line[:current_position] + (current_char == tree and "X" or "O") + line[current_position + 1:])
			if current_char == tree:
				trees_counter += 1
		else:
			print(line)
	

	print()
	print("Trees:", trees_counter)
	print("———————————")
	print()

	return trees_counter


def solution01(input_list):
	return slope_check(input_list, 3)


def solution02(input_list):
	step_iterations = [ 
		(1,1), 
		(3,1), 
		(5,1), 
		(7,1), 
		(1,2)
	]

	output_product = 0

	for steps in step_iterations:
		trees = slope_check(input_list, steps[0], steps[1])
		output_product = output_product != 0 and output_product * trees or trees

	return output_product


solution01_start_time = time.time()
solution01 = solution01(input_list)
solution01_total_time = time.time() - solution01_start_time

solution02_start_time = time.time()
solution02 = solution02(input_list)
solution02_total_time = time.time() - solution02_start_time

print("Solution 01:", solution01, "in", solution01_total_time)
print("Solution 02:", solution02, "in", solution02_total_time )

