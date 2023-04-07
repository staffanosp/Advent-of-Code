import time
import math
import itertools


with open("input.txt","r") as f:
	input = [i.strip().split(" = ") for i in f.readlines()]

	#for i in input: print(i)

def to_bits(num):
	bits = 36
	return bin(num)[2:].zfill(bits)

def to_decimal(bits):
	return int(bits, 2)

def solution01(program):

	mem = {}
	mask = ""

	for line in program:
		if line[0] == "mask":
			mask = line[1]
			print(mask)
		else:
			address = int(line[0][4:-1])
			v = int(line[1])
			v_bits = to_bits(v)
			result = v_bits

			#overwrite the values from the mask
			for i, bit in enumerate(mask):
				if bit != "X":
					result = result[:i] + bit + result[i+1:]
					

			print(address, v)
			print(v_bits)
			print(mask)
			print(result)
			print(to_decimal(result))
			print("———————")

			mem[address] = to_decimal(result)

	print(len(mem))
	return sum(mem.values())

def solution02(program):

	mem = {}
	mask = ""
	writes_counter = 0


	for line in program:
		if line[0] == "mask":
			mask = line[1]
			print(mask)
		else:
			address = int(line[0][4:-1])
			address_bits = to_bits(address)

			v = int(line[1])
			print(address_bits)
			#apply bitmask
			for i, bit in enumerate(mask):
				if bit != "0":
					address_bits = address_bits[:i] + bit + address_bits[i+1:]
					

			print(address_bits)
			print(mask)
			print("———————")


			#do the floats and write to every adress
			floats_n = address_bits.count("X")

			float_combinations = [i for i in itertools.product(range(2), repeat=floats_n)]

			
			for combination in float_combinations:
				address_bits_temp = address_bits
				x_index = 0
				for i, bit in enumerate(address_bits_temp):
					if bit == "X":
						address_bits_temp = address_bits_temp[:i] + str(combination[x_index]) + address_bits_temp[i+1:]
						x_index += 1

				print(address_bits_temp, to_decimal(address_bits_temp))
				writes_counter += 1
				mem[address_bits_temp] = v
			
			print("———————")




			#break
			
	
	print(len(mem))
	print("Writes", writes_counter)
	return sum(mem.values())

solution01_start_time = time.time()
solution01_result = solution01(input)
solution01_time = time.time() - solution01_start_time



solution02_start_time = time.time()
solution02_result = solution02(input)
solution02_time = time.time() - solution02_start_time

print("Solution 01:", solution01_result, "in", solution01_time)
print("Solution 02:", solution02_result, "in", solution02_time)


