import time
import math

with open("input.txt","r") as f:
	instructions = [i.strip() for i in f.readlines()]




def solution01(instructions):

	ship_x, ship_y = 0, 0
	ship_rotation = 90

	for instruction in instructions:
		action, value = instruction[:1], int(instruction[1:])

		if action == "N" or (action == "F" and ship_rotation == 0):
			ship_y -= value
		elif action == "S" or (action == "F" and ship_rotation == 180):
			ship_y += value
		elif action == "E" or (action == "F" and ship_rotation == 90):
			ship_x += value
		elif action == "W" or (action == "F" and ship_rotation == 270):
			ship_x -= value
		elif action == "L":
			ship_rotation = (ship_rotation - value) % 360
		elif action == "R":
			ship_rotation = (ship_rotation + value) % 360

		print("——————")
		print(action, value)
		print(ship_x, ship_y)
		print(ship_rotation)

	return abs(ship_x) + abs(ship_y)


def solution02(instructions):

	ship_x, ship_y = 0, 0
	wp_x, wp_y = 10, -1


	for instruction in instructions:
		action, value = instruction[:1], int(instruction[1:])

		if action == "N":
			wp_y -= value
		elif action == "S":
			wp_y += value
		elif action == "E":
			wp_x += value
		elif action == "W":
			wp_x -= value
		
		elif action == "L":
			wp_x_old = wp_x
			wp_y_old = wp_y

			if value == 90:
				wp_x = wp_y_old
				wp_y = wp_x_old * -1

			elif value == 180:
				wp_x = wp_x_old * -1
				wp_y = wp_y_old * -1

			elif value == 270:
				wp_x = wp_y_old * -1
				wp_y = wp_x_old 

		
		elif action == "R":
			wp_x_old = wp_x
			wp_y_old = wp_y

			if value == 90:
				wp_x = wp_y_old * -1
				wp_y = wp_x_old

			elif value == 180:
				wp_x = wp_x_old * -1
				wp_y = wp_y_old * -1

			elif value == 270:
				wp_x = wp_y_old
				wp_y = wp_x_old * -1

		elif action == "F":
			ship_x = ship_x + wp_x * value
			ship_y = ship_y + wp_y * value

		print("——————")
		print(action, value)
		print(ship_x, ship_y)
		#print(ship_rotation)

	return abs(ship_x) + abs(ship_y)



#solution01_start_time = time.time()
#solution01_result = solution01(instructions)
#solution01_time = time.time() - solution01_start_time

solution02_start_time = time.time()
solution02_result = solution02(instructions)
solution02_time = time.time() - solution02_start_time

#print("Solution 01:", solution01_result, "in", solution01_time)
print("Solution 02:", solution02_result, "in", solution02_time)
