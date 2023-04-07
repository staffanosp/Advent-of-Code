import time

with open("input.txt","r") as file:
    paper = set()
    folds = []
    part = 0

    for line in (line.strip()for line in file):

        if line == "":
            part += 1
            continue

        if part == 0:
            x,y = line.split(',')
            paper.add((int(x),int(y)))

        if part == 1:
            _,_,fold = line.split()
            axis, pos = fold.split('=')

            folds.append((axis,int(pos)))


#I had already written this fance print function (including printing of folds) for debugging of part 1..
def print_paper(paper, fold = False):
    min_x = min([x for (x,y) in paper])
    max_x = max([x for (x,y) in paper])
    min_y = min([y for (x,y) in paper])
    max_y = max([y for (x,y) in paper])
    
    print()

    for y in range(min_y,max_y+1):
        print(f'{y:>5}',end="  ")
        for x in range(min_x,max_x+1):
            if (x,y) in paper:
                to_print = "#"
            else:
                to_print = "."

            if fold:
                if fold[0] == 'y' and fold[1] == y:
                    to_print = '—'
                elif fold[0] == 'x' and fold[1] == x:
                    to_print = '|'
            else:
                if (x,y) in paper:
                    to_print = "#"
                else:
                    to_print = " "
                    
            print(to_print, end='')
        print()
    print()


    


def solution(paper,folds,part):

    for axis,pos in folds:

        if axis == 'x':
            axis_i = 0
        elif axis == 'y':
            axis_i = 1

        a = set(xy for xy in paper if xy[axis_i] < pos)
        b = set((pos - (x-pos) if axis == 'x' else x, pos - (y-pos) if axis == 'y' else y) for (x,y) in paper if (x,y)[axis_i] > pos)
        paper = a|b

        if part == 1: #part 1 returns after first iteration
            return len(paper)

    #print the paper for part 2
    print_paper(paper)

    return 


solution01_start_time = time.time()
solution01 = solution(paper.copy(),folds,1)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution(paper.copy(),folds,2)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: (see print above ^^^), in {solution02_total_time}")