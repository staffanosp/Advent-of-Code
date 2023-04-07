import time

with open("input.txt","r") as file:
    input_data = [line.strip().split('-') for line in file]

caves = {}
for row in input_data:
    for i in range(2):
        if not row[i] in caves:
            caves[row[i]] = []
        caves[row[i]].append(row[(i+1) % 2])


def solution01(caves):

    def find_paths(path):
        ok_paths = []
        
        def find_path_recurse(path):
            for connecting_cave in caves[path[-1]]:
                if connecting_cave == 'end':
                    ok_paths.append(path + [connecting_cave])
                
                if not connecting_cave == 'start' and not connecting_cave == 'end' and not (connecting_cave.islower() and connecting_cave in path):
                    find_path_recurse(path + [connecting_cave])
        
        find_path_recurse(path)
        
        return ok_paths


    return len(find_paths(['start']))


def solution02(caves):

    def find_paths(path):
        ok_paths = []

        def find_path_recurse(path, visited_small_cave_twice = False):
            #check if a double visit to a small cave has happened
            if path[-1].islower() and path[-1] in path[:-1]:
                visited_small_cave_twice = True

            for connecting_cave in caves[path[-1]]:
                if connecting_cave == 'end':
                    ok_paths.append(path + [connecting_cave])
                
                if not connecting_cave == 'start' and not connecting_cave == 'end' and not (connecting_cave.islower() and connecting_cave in path and visited_small_cave_twice):
                    find_path_recurse(path + [connecting_cave],visited_small_cave_twice)
        
        find_path_recurse(path)
        
        return ok_paths


    return len(find_paths(['start']))


solution01_start_time = time.time()
solution01 = solution01(caves)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(caves)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")