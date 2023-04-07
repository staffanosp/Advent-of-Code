import time

with open("input.txt","r") as file:
    input_list = [[int(x) for x in line.strip().split(',')] for line in file][0]

def solution(input_list,days):
    all_fish = [0] * 9

    for fish in input_list:
        all_fish[fish] += 1
    
    for day in range(days):
        temp_all_fish = [0] * 9
        new_fish = 0
        
        for age, _ in enumerate(all_fish):
            if age == 0:
                temp_all_fish[8] = all_fish[age]
                temp_all_fish[age] = 0
            else:
                temp_all_fish[age-1] = all_fish[age]
                if age < 8:
                    temp_all_fish[age] = 0

        temp_all_fish[6] += all_fish[0] 

        all_fish = temp_all_fish.copy()

    return sum(all_fish)


solution01_start_time = time.time()
solution01 = solution(input_list,80)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution(input_list,256)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")