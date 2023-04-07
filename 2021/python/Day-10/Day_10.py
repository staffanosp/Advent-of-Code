import time

with open("input.txt","r") as file:
    input_data = [line.strip()for line in file]

def solution01(input_data):
    
    def get_opener(closer):
        for a,b in chunk_pairs.items():
            if b == closer:
                return a

    chunk_pairs = {   '(':')','[':']','{':'}','<':'>'}
    chunk_openers = [x for x in chunk_pairs]
    chunk_closers = [x for x in chunk_pairs.values()]
    error_scores = { ')':3,']':57,'}':1197,'>':25137 }
    corrupt_closers = []

    for line in input_data:
        chunk_stack = []

        for char in line:
            if char in chunk_openers:
                chunk_stack.append(char)
                continue

            if char in chunk_closers:
                if chunk_stack:
                    last_opener = chunk_stack.pop()

                    if not get_opener(char) == last_opener:
                        corrupt_closers.append(char)
                        break

                else:   #empty stack
                    corrupt_closers.append(char)
                    break

    total_error_score = 0
    for closer in corrupt_closers:
        total_error_score += error_scores[closer]
    
    return total_error_score


def solution02(input_data):
    
    def get_opener(closer):
        for a,b in chunk_pairs.items():
            if b == closer:
                return a

    chunk_pairs = {   '(':')','[':']','{':'}','<':'>'}
    chunk_openers = [x for x in chunk_pairs]
    chunk_closers = [x for x in chunk_pairs.values()]
    error_scores = { ')':1,']':2,'}':3,'>':4 }
    all_completions = []

    for line in input_data:
        chunk_stack = []
        corrupt = False

        for char in line:
            if char in chunk_openers:
                chunk_stack.append(char)
                continue

            if char in chunk_closers:
                if chunk_stack:
                    last_opener = chunk_stack.pop()

                    if not get_opener(char) == last_opener:
                        corrupt = True
                        break

                else:   #empty stack
                    corrupt = True
                    break

        if not corrupt:
            current_completion = []
            while len(chunk_stack) > 0:
                last_opener = chunk_stack.pop()
                current_completion.append(chunk_pairs[last_opener])
            all_completions.append(current_completion)
            

    #count the scores per line
    line_scores = []
    for line in all_completions:
        line_score = 0
        for char in line:
            line_score *= 5
            line_score += error_scores[char]
        line_scores.append(line_score)

    return sorted(line_scores)[len(line_scores) // 2]


solution01_start_time = time.time()
solution01 = solution01(input_data)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(input_data)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")