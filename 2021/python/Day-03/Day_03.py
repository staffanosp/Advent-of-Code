import time

with open("input.txt","r") as file:
    input_list = [line.strip() for line in file]

def solution01(input_list):
    gamma, epsilon = "",""
    length = len(input_list[0])

    for i in range(length):
        curr_bits = [bits[i] for bits in input_list]

        count_0 = curr_bits.count("0")
        count_1 = curr_bits.count("1")

        new_gamma_bit = "0" if count_0 > count_1 else "1"
        new_epsilon_bit = "0" if new_gamma_bit == "1" else "1"

        gamma += new_gamma_bit
        epsilon += new_epsilon_bit


    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")

    return int(gamma, 2) * int(epsilon, 2)

def solution02(input_list):

    def bit_criteria(bits, mode):
        bits_left = [i for i in bits]
    
        i = 0
        while len(bits_left) > 1:

            curr_bits = [bits[i] for bits in bits_left]

            count_0 = curr_bits.count("0")
            count_1 = curr_bits.count("1")

            if mode == "most":
                bit_to_keep = "1" if count_1 >= count_0 else "0"
            elif mode == "least":
                bit_to_keep = "0" if count_0 <= count_1 else "1"
            
            bits_left = [v for v in bits_left if v[i] == bit_to_keep]

            i += 1

        return bits_left[0]

    oxygen = bit_criteria(input_list, "most")
    co2 = bit_criteria(input_list, "least")

    print(f"oxygen: {oxygen}")
    print(f"co2: {co2}")

    return int(oxygen, 2) * int(co2, 2)


solution01_start_time = time.time()
solution01 = solution01(input_list)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(input_list)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")

