import time
from collections import Counter

with open("input.txt","r") as file:
    template = []
    rules = {}
    part = 0

    for line in (line.strip()for line in file):

        if line == "":
            part += 1
            continue

        if part == 0:
            template = [c for c in line]

        elif part == 1:
            pair,to_insert = line.split(' -> ')
            rules[pair] = to_insert


print(template)
print(rules)


def solution(template,rules,steps):
    polymer = template[:]

    for step in range(steps):
        print('step',step)
        new_polymer = []
        for i in range(len(polymer)):
            
            
            if i == len(polymer)-1:
                new_polymer.append(polymer[i])
                continue

            pair = polymer[i] + polymer[i+1]
            #print(pair)
            if pair in rules:
                new_polymer.append(polymer[i])
                new_polymer.append(rules[pair])
            else:
                print("not in rules:", pair)
            
            #print('new',new_polymer)

        polymer = new_polymer
        #print(polymer)
        print("polymer len", len(polymer))

    polymer_counter = Counter(polymer)
    print('most common', polymer_counter.most_common()[0])
    print('least common', polymer_counter.most_common()[-1])



    my_list = [1]*1000
    print(my_list)
    #for i in range(2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602*2192039569602):
    #    print(i)


    return polymer_counter.most_common()[0][1] - polymer_counter.most_common()[-1][1]


solution01_start_time = time.time()
solution01 = solution(template,rules,10)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

#solution02_start_time = time.time()
#solution02 = solution(template,rules,40)
#solution02_total_time = time.time() - solution02_start_time
#print(f"Solution 02: (see print above ^^^), in {solution02_total_time}")