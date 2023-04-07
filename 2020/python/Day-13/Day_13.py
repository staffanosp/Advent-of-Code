import time
import math

with open("input.txt","r") as f:
	#input = [i.strip() for i in f.readlines()]

	earliest_departure = int(f.readline().strip())
	buses = [bus for bus in f.readline().strip().split(",")]




def ceiling_division(n, d):
    return -(n // -d)

def solution01(earliest_departure, buses):

	buses = [int(bus) for bus in buses if not bus == "x"]

	earliest_bus_departure = 0
	earliest_bus_id = 0

	for bus in buses:
		earliest_departure_for_bus = math.ceil(earliest_departure / bus) * bus

		if earliest_departure_for_bus < earliest_bus_departure or earliest_bus_departure == 0:
			earliest_bus_departure = earliest_departure_for_bus
			earliest_bus_id = bus
	
	return (earliest_bus_departure - earliest_departure) * earliest_bus_id

def solution02(earliest_departure, buses):
	for i in range(100000000000000):
		print(i)

	return i

solution01_start_time = time.time()
solution01_result = solution01(earliest_departure, buses)
solution01_time = time.time() - solution01_start_time

print("Solution 01:", solution01_result, "in", solution01_time)

solution02_start_time = time.time()
solution02_result = solution02(earliest_departure, buses)
solution02_time = time.time() - solution02_start_time


print("Solution 02:", solution02_result, "in", solution02_time)


