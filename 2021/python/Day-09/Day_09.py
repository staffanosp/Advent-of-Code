import time
import math


with open("input.txt","r") as file:
    input_data = [[int(num) for num in line.strip()] for line in file]
    print(input_data)
    
def solution01(map):
    width = len(map[0])
    height = len(map)

    low_points =[]
    for y, _ in enumerate(map):
        for x, _ in enumerate(map[y]):
            
            adjacent_values = []

            #left
            if x > 0:
                adjacent_values.append(map[y][x-1])

            #right
            if x < width-1:
                adjacent_values.append(map[y][x+1])

            #up
            if y > 0:
                adjacent_values.append(map[y-1][x])

            #down
            if y < height-1:
                adjacent_values.append(map[y+1][x])

            if all(map[y][x] < adjacent_v for adjacent_v in adjacent_values):
                low_points.append(map[y][x])

    return sum([v+1 for v in low_points])



def solution02(map):
    width = len(map[0])
    height = len(map)

    has_been_checked = set()
    has_been_checked_w_basin_n = {}
    basins = []

    for x,y in ((x,y) for x in range(width) for y in range(height)):
        if map[y][x] == 9 or (x,y) in has_been_checked:
            continue

        current_basin = {(x,y)}
        prev_current_basin_length = 0

        #loop over and add points to current basin until the size of the basin stops expanding
        while len(current_basin) != prev_current_basin_length:
            add_to_current_basin = set()
            for coords in current_basin:
                if coords in has_been_checked:
                    continue

                #add adj coords, if not 9
                #left
                if coords[0] > 0:
                    if not map[coords[1]][coords[0]-1] == 9:
                        add_to_current_basin.add((coords[0]-1, coords[1]))
                
                #right
                if coords[0] < width-1:
                    if not map[coords[1]][coords[0]+1] == 9:
                        add_to_current_basin.add((coords[0]+1, coords[1]))

                
                #up
                if coords[1] > 0:
                    if not map[coords[1]-1][coords[0]] == 9:
                        add_to_current_basin.add((coords[0], coords[1]-1))
                
                #down
                if coords[1] < height-1:
                    if not map[coords[1]+1][coords[0]] == 9:
                        add_to_current_basin.add((coords[0], coords[1]+1))

                has_been_checked.add(coords)

            prev_current_basin_length = len(current_basin)
            current_basin |= add_to_current_basin

        basins.append(current_basin)

    return math.prod(sorted([len(basin )for basin in basins])[-3:])


solution01_start_time = time.time()
solution01 = solution01(input_data)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(input_data)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")
