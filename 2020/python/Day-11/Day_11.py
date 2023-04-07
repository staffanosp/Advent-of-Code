import time

with open("input.txt","r") as f:
	input_list = [i.strip() for i in f.readlines()]

FLOOR = "."
SEAT_EMPTY = "L"
SEAT_OCCUPIED = "#"


def print_seat_layout(seat_layout):
	for row in seat_layout:
		print(row)
	print("———")

def count_adj_occupied_seats(seat_layout, row, seat, solution):
	counter = 0
	max_rows = len(seat_layout) - 1
	max_seats = len(seat_layout[0]) - 1

	if solution == 1:
		#print("adj")
		#print(seat_layout[0][0])
		for row_d in range(-1, 2):
			#guard: make sure row is within range
			if not 0 <= row + row_d <= max_rows: continue

			for seat_d in range(-1,2):
				#guard: make sure seat is within range
				if not 0 <= seat + seat_d <= max_seats: continue

				#don't compare to itself
				if row_d == 0 and seat_d == 0: continue

				#print(row_d, seat_d)
				#print(row + row_d, seat + seat_d, seat_layout[row + row_d][seat + seat_d])
				if seat_layout[row + row_d][seat + seat_d] == SEAT_OCCUPIED:
					counter += 1
	elif solution == 2:
		for row_d in range(-1, 2):
			for seat_d in range(-1,2):
				#guard: continue if delta is 0,0
				if row_d == 0 and seat_d == 0: continue

				i = 0

				while True:
					row_check = row + row_d * (i+1)
					seat_check = seat + seat_d * (i+1)

					#break if out of range
					if not 0 <= row_check <= max_rows or not 0 <= seat_check <= max_seats: 
						break

					#print_seat_layout(seat_layout)

					if seat_layout[row_check][seat_check] == SEAT_EMPTY:
						break

					if seat_layout[row_check][seat_check] == SEAT_OCCUPIED:
						counter += 1
						break

					i += 1
			
	#print("counter", counter)
	return counter


def check_seat_layout(seat_layout, solution):
	new_seat_layout = []
	min_adj_occupied_seats = 4 if solution == 1 else 5

	for row_i, row in enumerate(seat_layout):
		new_row = ""
		for seat_i, seat in enumerate(row):
			new_seat = seat
			if not seat == FLOOR:
				adj_occupied_seats = count_adj_occupied_seats(seat_layout, row_i, seat_i, solution)
			
			if seat == SEAT_EMPTY and adj_occupied_seats == 0:
				new_seat = SEAT_OCCUPIED
			elif seat == SEAT_OCCUPIED and adj_occupied_seats >= min_adj_occupied_seats:
				new_seat = SEAT_EMPTY
			#new_seat = f"{str(counter)} "
			#new_seat = f"{str(adj_occupied_seats)} "

			new_row += new_seat
		new_seat_layout.append(new_row)
	return new_seat_layout

def solution01(seat_layout):



	prev_seat_layout = seat_layout

	stable_layout = False
	while not stable_layout:
		new_seat_layout = check_seat_layout(prev_seat_layout, 1)

		print_seat_layout(prev_seat_layout)
		
		print_seat_layout(new_seat_layout)
		if new_seat_layout == prev_seat_layout:
			stable_layout = True

		prev_seat_layout = new_seat_layout
	
	#count occupied seats
	counter = 0
	for row in new_seat_layout:
		counter += row.count(SEAT_OCCUPIED)

	
	return counter


def solution02(seat_layout):



	prev_seat_layout = seat_layout

	stable_layout = False
	while not stable_layout:
		new_seat_layout = check_seat_layout(prev_seat_layout, 2)

		print_seat_layout(prev_seat_layout)
		
		print_seat_layout(new_seat_layout)
		if new_seat_layout == prev_seat_layout:
			stable_layout = True

		prev_seat_layout = new_seat_layout

		#stable_layout = True
	
	#count occupied seats
	counter = 0
	for row in new_seat_layout:
		counter += row.count(SEAT_OCCUPIED)

	
	return counter



solution01_start_time = time.time()
solution01_result = solution01(input_list)
solution01_time = time.time() - solution01_start_time

solution02_start_time = time.time()
solution02_result = solution02(input_list)
solution02_time = time.time() - solution02_start_time

#print("Solution 01:", solution01_result, "in", solution01_time)
print("Solution 02:", solution02_result, "in", solution02_time)
