import time

with open("input.txt","r") as file:
    input_data = [[int(c) for c in line.strip()] for line in file]



def print_map(map, step = 0):
    if step:
        print("—————— STEP:", step )
    else:
        print("——————")

    
    for y in map:
        for x in y:
            print(f'{x:^4}',end='')
        print()


print_map(input_data)


def solution01(input_data):
    def count_flashes(map):
        flashes = 0
        for x,y in ((x,y) for x in range(w) for y in range(w)):
            if map[y][x] > 9:
                flashes += 1
        return flashes

    map = input_data
    w,h = len(input_data[0]), len(input_data)
    steps = 1


    for step in range(steps):
        coords_to_check = []

        #up energy with 1
        for x,y in ((x,y) for x in range(w) for y in range(w)):
            map[y][x] += 1
            coords_to_check.append((x,y))

        # up adj octopuses
        increased_flashes = True
        while increased_flashes:
            pre_flash_count = count_flashes(map)

            for x,y in ((x,y) for x in range(w) for y in range(w)):
                if map[y][x] > 9:
                    for adj_x,adj_y in [(x+add_x,y+add_y) for add_x in range(-1,2) for add_y in range(-1,2)]:
                        #don't up itself
                        if adj_x == x and adj_y == y:
                            continue

                        #check if out of range and make sure we're not checking 
                        if adj_x < 0 or adj_x > (w-1) or adj_y < 0 or adj_y > (h-1):
                            continue
                        
                        map[adj_y][adj_x] +=1


                    #up adj

            print_map(map,step + 1)
            print('pre_flash_count',pre_flash_count)
            print('count_flashes(map)',count_flashes(map))
            increased_flashes = bool(count_flashes(map) > pre_flash_count)

            #time.sleep(1)


        #set >9 to 0
        for x in range(w):
            for y in range(h):
                if map[y][x] > 9:
                    map[y][x] = 0


        print_map(map,step + 1)


    return


solution01_start_time = time.time()
solution01 = solution01(input_data)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

#solution02_start_time = time.time()
#solution02 = solution02(input_data)
#solution02_total_time = time.time() - solution02_start_time
#print(f"Solution 02: {solution02}, in {solution02_total_time}")