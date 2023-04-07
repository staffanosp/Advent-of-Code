import time



with open("input.txt","r") as file:
    input_data = [{'signal':line[0].split(), 'output':line[1].split()} for line in (line.strip().split(" | ") for line in file)]


def solution01(input_data):
    unique_segment_counts = [2, 3, 4, 7]
    unique_counter = 0

    for entry in input_data:
        for output in entry['output']:
            if len(output) in unique_segment_counts:
                unique_counter += 1
    return unique_counter


def solution02(input_data):
    segments_to_numbers = { 'abcefg':0,
                            'cf':1,
                            'acdeg':2,
                            'acdfg':3,
                            'bcdf':4,
                            'abdfg':5,
                            'abdefg':6,
                            'acf':7,
                            'abcdefg':8,
                            'abcdfg':9}

    all_outputs = []

    for entry in input_data:
        signals_by_segment_count = {i:[] for i in range(2,8)}

        #sort signal by segment count
        for signal in entry['signal']:
            signals_by_segment_count[len(signal)].append(signal)

        #find out the mapping
        signal_map = {}

        #1 segments are potential C F
        C_F = signals_by_segment_count[2][0]
        
        #the diff between 1 and 4 is potential B D
        B_D = ""
        for char in signals_by_segment_count[4][0]:
            if not char in signals_by_segment_count[2][0]:
                B_D  += char

        #the diff between 8 and (4+7) is potential E G
        E_G = ""
        for char in signals_by_segment_count[7][0]:
            if not char in set(char for char in (signals_by_segment_count[4][0] + signals_by_segment_count[3][0])):
                E_G  += char

        #the diff between 1 and 7 is segment A
        for char in signals_by_segment_count[3][0]:
            if not char in signals_by_segment_count[2][0]:
                signal_map[char] = 'a'


        #The char in B_D that is in 0,6 and 9 (segment count 6) is B, the other one is D
        if all([B_D[0] in signal for signal in signals_by_segment_count[6]]):
            signal_map[B_D[0]] = 'b'
            signal_map[B_D[1]] = 'd'
        else:
            signal_map[B_D[0]] = 'd'
            signal_map[B_D[1]] = 'b'

        #The char in C_F that is in 0,6 and 9 (segment count 6) is F, the other one is C
        if all([C_F[0] in signal for signal in signals_by_segment_count[6]]):
            signal_map[C_F[0]] = 'f'
            signal_map[C_F[1]] = 'c'
        else:
            signal_map[C_F[0]] = 'c'
            signal_map[C_F[1]] = 'f'


        #The char in E_G that is in 2,3 and 5 (segment count 5) is G, the other one is E
        if all([E_G[0] in signal for signal in signals_by_segment_count[6]]):
            signal_map[E_G[0]] = 'g'
            signal_map[E_G[1]] = 'e'
        else:
            signal_map[E_G[0]] = 'e'
            signal_map[E_G[1]] = 'g'

        #convert the output
        output_4_digit = ""
        for output in entry['output']:
            converted_output_list = sorted([signal_map[char] for char in output])
            converted_output = ""
            for char in converted_output_list:
                converted_output += char

            output_4_digit += str(segments_to_numbers[converted_output])
        
        all_outputs.append(int(output_4_digit))

    return sum(all_outputs)


solution01_start_time = time.time()
solution01 = solution01(input_data)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(input_data)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")#