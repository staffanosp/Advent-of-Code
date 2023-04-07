import time
import math

#parse input
with open("input.txt","r") as f:
	fields = {}
	my_ticket = []
	nearby_tickets = []

	parse_pass = "fields"

	for line in [line.strip() for line in f.readlines()]:

		if line == "":
			continue
		if line == "your ticket:":
			parse_pass = "my_ticket"
			continue
		if line == "nearby tickets:":
			parse_pass = "nearby_tickets"
			continue

		if parse_pass == "fields":
			field, ranges = line.split(": ")
			lower, upper = ranges.split(" or ")

			lower = tuple([int(i) for i in lower.split("-")])
			upper = tuple([int(i) for i in upper.split("-")])

			print(field, lower, upper)
			fields[field] = [lower, upper]

		elif parse_pass == "my_ticket":
			my_ticket = [int(i) for i in line.split(",")]

		elif parse_pass == "nearby_tickets":
			nearby_tickets.append([int(i) for i in line.split(",")])

	print("—————")
	print(fields)
	print(my_ticket)
	print(nearby_tickets)
	print("—————")

def get_all_ranges(fields):
	all_ranges = []

	for field in fields:
		for field_range in fields[field]:
			for i in range(field_range[0], field_range[1] + 1):
				all_ranges.append(i)

	return set(all_ranges)



def solution01(fields, my_ticket, nearby_tickets):
	all_ranges = get_all_ranges(fields)

	scanning_error_rate = 0
	scanning_error_count = 0

	for ticket in nearby_tickets:
		for num in ticket:
			if not num in all_ranges:
				scanning_error_rate += num
				scanning_error_count += 1

	print("scanning_error_count", scanning_error_count)
	print("scanning_error_rate", scanning_error_rate)
	
	return scanning_error_rate




def solution02(fields, my_ticket, nearby_tickets):
	all_ranges = get_all_ranges(fields)

	scanning_error_rate = 0
	scanning_error_count = 0

	nearby_tickets_valid = []
	for ticket in nearby_tickets:

		valid = True
		for num in ticket:
			if not num in all_ranges:
				valid = False
				scanning_error_rate += num
				scanning_error_count += 1

		if valid:
			nearby_tickets_valid.append(ticket)

	field_positions = {}


	for field in fields:
		

		lower_min, lower_max = fields[field][0]
		upper_min, upper_max = fields[field][1]

		print(field)
		print(lower_min, lower_max)
		print(upper_min, upper_max)

		for pos in range(len(my_ticket)):
			#skip if pos is already found
			print("     pos:" + str(pos))
			for ticket in nearby_tickets:
				print("     " + "     " + str(ticket[pos]))
#				print("ticket[pos]", ticket[pos])
				if not lower_min <= ticket[pos] <= lower_max and not upper_min <= ticket[pos] <= upper_max:
					print("break")
#					break
					

#			field_positions[field] = pos

#		print(field_positions)

		print("—————")

	
	return


#solution01_start_time = time.time()
#solution01_result = solution01(fields, my_ticket, nearby_tickets)
#solution01_time = time.time() - solution01_start_time
#
#print("Solution 01:", solution01_result, "in", solution01_time)

solution02_start_time = time.time()
solution02_result = solution02(fields, my_ticket, nearby_tickets)
solution02_time = time.time() - solution02_start_time


print("Solution 02:", solution02_result, "in", solution02_time)


