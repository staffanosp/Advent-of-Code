import time

#bright white bags contain 1 shiny gold bag.
#vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
#dotted black bags contain no other bags.


with open("input.txt","r") as f:
	in_data = {}
	for kv in f.readlines():
		k, v = kv.strip().split(" contain ")

		def cleanup_input(in_string, is_key):
			#if is_key, there is no number in the beginning
			tmp_list = in_string.split()
			if is_key:
				return tmp_list[0] + " " + tmp_list[1]
			else:
				return tmp_list[1] + " " + tmp_list[2]

		if v == "no other bags.":
			v = []
		else:
			v = [cleanup_input(v, False) for v in v.split(",")] #

		in_data[cleanup_input(k, True)] = v




def can_contain(rules, outer, search):
    for bag in rules[outer]:
        if bag == search:
            return True

        if can_contain(rules, bag, search):
            return True

    return False




def solution01(bags):
	search = "shiny gold"

	return len([bag for bag in bags if can_contain(bags, bag, search)])




solution01_start_time = time.time()
solution01 = solution01(in_data)
solution01_total_time = time.time() - solution01_start_time
#
#solution02_start_time = time.time()
#solution02 = solution02(boarding_passes)
#solution02_total_time = time.time() - solution02_start_time
#
print("Solution 01:", solution01, "in", solution01_total_time)
#print("Solution 02:", solution02, "in", solution02_total_time)
#