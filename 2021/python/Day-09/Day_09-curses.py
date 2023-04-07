import time
import math
import os
import curses
import random
with open("input.txt","r") as file:
    input_data = [[int(num) for num in line.strip()] for line in file]




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



def main(stdscr,map,random_map):
    if random_map:
        map_size = 80
        map = []
        rate_9 = random.randint(1, 3)

        for y in range(map_size):
            line = []
            for x in range(map_size):
                if not random.randint(0, rate_9):
                    new_num = 9
                else:
                    new_num = random.randint(0, 8)
                    
                line.append(new_num)
            map.append(line)

    width = len(map[0])
    height = len(map)
    print_char_w = 3
    pad = curses.newpad(height+1,width*print_char_w+1)

    color_pairs = [ (curses.COLOR_BLACK,curses.COLOR_RED),
                    (curses.COLOR_BLACK,curses.COLOR_GREEN),
                    (curses.COLOR_BLACK,curses.COLOR_YELLOW),
                    (curses.COLOR_BLACK,curses.COLOR_BLUE),
                    (curses.COLOR_BLACK,curses.COLOR_MAGENTA),
                    (curses.COLOR_BLACK,curses.COLOR_CYAN),

    ]

    for i, color_pair in enumerate(color_pairs):
        curses.init_pair(i+1, color_pair[0],color_pair[1])

    color_start = random.randint(0, len(color_pairs))


    #print default grid
    grid_char = "."
    for x,y in ((x,y) for x in range(width) for y in range(height)):
        to_print = grid_char #map[y][x]
        pad.addstr(y, x*print_char_w, f'{to_print:^{print_char_w}}', curses.A_DIM)
    pad.refresh( 0,0, 0,0, curses.LINES-1,curses.COLS-1)



    has_been_checked = set()
    has_been_checked_w_basin_n = {}
    basins = []

    x_list = [x for x in range(width)]
    random.shuffle(x_list)
    y_list = [y for y in range(height)]
    random.shuffle(y_list)

    xy_set = set(zip(x_list,y_list))

    while len(xy_set) > 0:

        x,y = xy_set.pop()
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
                        xy_set.discard((coords[0]-1, coords[1]))
                #right
                if coords[0] < width-1:
                    if not map[coords[1]][coords[0]+1] == 9:
                        add_to_current_basin.add((coords[0]+1, coords[1]))
                        xy_set.discard((coords[0]+1, coords[1]))

                
                #up
                if coords[1] > 0:
                    if not map[coords[1]-1][coords[0]] == 9:
                        add_to_current_basin.add((coords[0], coords[1]-1))
                        xy_set.discard((coords[0], coords[1]-1))
                
                #down
                if coords[1] < height-1:
                    if not map[coords[1]+1][coords[0]] == 9:
                        add_to_current_basin.add((coords[0], coords[1]+1))
                        xy_set.discard((coords[0], coords[1]+1))

                has_been_checked_w_basin_n[coords] = len(basins)
                has_been_checked.add(coords)
                #print_checked(width,height,has_been_checked_w_basin_n)




                #PRINT!
                basin_i = len(basins) + 1
                color_i = (basin_i + color_start) % (len(color_pairs)) + 1
                to_print = basin_i #map[coords[1]][coords[0]]
                pad.addstr(coords[1], coords[0]*print_char_w, f'{to_print:^{print_char_w}}', curses.color_pair(color_i))
                pad.refresh( 0,0, 0,0, curses.LINES-1,curses.COLS-1)
                time.sleep(0.001)




            prev_current_basin_length = len(current_basin)
            current_basin |= add_to_current_basin




        basins.append(current_basin)
    #print_checked(width,height,has_been_checked_w_basin_n)

    time.sleep(1)
    return math.prod(sorted([len(basin )for basin in basins])[-3:])


#solution01_start_time = time.time()
#solution01 = solution01(input_data)
#solution01_total_time = time.time() - solution01_start_time
#print(f"Solution 01: {solution01}, in {solution01_total_time}")
#
#solution02_start_time = time.time()
#solution02 = solution02(input_data)
#solution02_total_time = time.time() - solution02_start_time
#print(f"Solution 02: {solution02}, in {solution02_total_time}")


while True:
    curses.wrapper(main,input_data,True)

