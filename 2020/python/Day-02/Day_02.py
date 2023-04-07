f = open("input.txt","r")
input_list = [i for i in f.readlines()]
f.close()

def format_input(input_string):
	numbers, letter, password = input_string.split()
	first_num, second_num = numbers.split("-")
	first_num = int(first_num)
	second_num = int(second_num)
	letter = letter[:1]

	return first_num, second_num, letter, password


def solution01(input_list):
	ok_passwords = 0

	for i in input_list:
		min_times, max_times, letter, password = format_input(i)

		if min_times <= password.count(letter) <= max_times:
			ok_passwords += 1
	
	return ok_passwords


def solution02(input_list):
	ok_passwords = 0

	for i in input_list:
		nr_of_occurrences_in_positions = 0
		pos01, pos02, letter, password = format_input(i)

		if password[pos01 - 1] == letter:
			nr_of_occurrences_in_positions += 1

		if password[pos02 - 1] == letter:
			nr_of_occurrences_in_positions += 1

		if nr_of_occurrences_in_positions == 1:
			ok_passwords += 1

	return ok_passwords

print("Solution 01:", solution01(input_list))
print("Solution 02:", solution02(input_list))
