import time

with open("input.txt","r") as f:
	in_data = []
	for line in f.readlines():
		operation, argument =line.split()
		in_data.append((operation, int(argument)))

def run_instructions(instructions):

	accumulator  = 0
	read_pos = 0
	executed_instructions = set()

	while read_pos <= len(instructions) - 1:
		if not read_pos in executed_instructions:
			operation, argument = instructions[read_pos]

			executed_instructions.add(read_pos)

			if operation == "acc":
				accumulator += argument
				read_pos += 1
			elif operation == "jmp": 
				read_pos += argument
			elif operation == "nop": 
				read_pos += 1
		
		else:
			#Tried to run the same operation twice
			return accumulator, False

	#Instructions terminated normally
	return accumulator, True


def solution01(instructions):
	return run_instructions(instructions)


def solution02(instructions):

	terminated_normally = False
	i = 0
	while not terminated_normally:
		operation, argument = instructions[i]
		
		if not operation == "acc":
			
			if operation == "jmp":
				updated_operation = "nop"
			elif operation == "nop":
				updated_operation = "nop"
		
			updated_instructions = instructions.copy()
			updated_instructions[i] = (updated_operation, updated_instructions[i][1])
			accumulator, terminated_normally = run_instructions(updated_instructions)
		
		i += 1
	return accumulator, terminated_normally



solution01_start_time = time.time()
print("Solution 01:", solution01(in_data), "in", time.time() - solution01_start_time)

solution02_start_time = time.time()
print("Solution 02:", solution02(in_data), "in", time.time() - solution02_start_time)