import time

with open("input.txt","r") as f:
	in_data = [ group.split("\n") for group in f.read().split("\n\n")]

	for i_g, group in enumerate(in_data):
		for i_p, person in enumerate(group):
			in_data[i_g][i_p] = {answer for answer in person}



def solution01(in_data):
	persons_answers = []
	for group in in_data:
		for person in group:
			for answer in person:
				persons_answers.append(answer)

	return len(list(dict.fromkeys(persons_answers)))


def solution02(in_data):
	yes_counter = 0

	for group in in_data:
		group_all_yes = set()

		for i, person in enumerate(group):
			if i == 0: 
				#for the first person, all answers are OK
				group_all_yes = person
			else:
				group_all_yes = group_all_yes.intersection(person)

		yes_counter += len(group_all_yes)

	return yes_counter


solution01_start_time = time.time()
solution01 = solution01(in_data)
solution01_total_time = time.time() - solution01_start_time

solution02_start_time = time.time()
solution02 = solution02(in_data)
solution02_total_time = time.time() - solution02_start_time

print("Solution 01:", solution01, "in", solution01_total_time)
print("Solution 02:", solution02, "in", solution02_total_time )

