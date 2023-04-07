import time

with open("input.txt","r") as f:
	#password batches to strings in list
	passports = [line.replace("\n"," ") for line in f.read().split("\n\n")]

	#password batches from strings to list
	for i in range(len(passports)):
		passports[i] = passports[i].split()

	#password list to dicts
	for line, batch_list in enumerate(passports):
		batch_dict = {}
		for i, k_v in enumerate(batch_list):
			k, v = k_v.split(":")
			batch_dict.update({ k: v })
		passports[line] = batch_dict


def validate_passport(passport, check_values = False):

	def check_number(v, min, max, length = False):
		if v.isdigit() and min <= int(v) <= max and (not length or len(v) == length):
			return True
		else:
			return False
	
	req_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
	
	for k in req_keys:
		#check if key exists
		if not k in passport: return False

		if check_values:
			v = passport[k]

			if k == "byr":
				if not check_number(v, 1920, 2002, 4): return False
		
			elif k == "iyr":
				if not check_number(v, 2010, 2020, 4): return False
		
			elif k == "eyr":
				if not check_number(v, 2020, 2030, 4): return False
		
			elif k == "hgt":
				unit = v[-2:]
				height = v[:-2]

				#check if unit is in or cm
				if unit == "cm":
					if not check_number(height, 150, 193): return False
				elif unit == "in":
					if not check_number(height, 59, 76): return False
				else: #return False if unit is invalid
					return False
		
			elif k == "hcl":
				first_char = v[0:1]
				rest_chars = v[1:]
			
				if not first_char == "#" or not all(c.isdigit() or c.islower() for c in rest_chars) or len(v) != 7: return False

			elif k == "ecl":
				if not v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False

			elif k == "pid":
				if not (v.isdigit() and len(v) == 9) : return False

	#nothing returned false, passport is valid
	return True

def solution01(passports):

	valid_passports_counter = 0

	for passport in passports:
		if validate_passport(passport):
			valid_passports_counter += 1

	return valid_passports_counter

def solution02(passports):

	valid_passports_counter = 0

	for passport in passports:
		if validate_passport(passport, True):
			valid_passports_counter += 1

	return valid_passports_counter




solution01_start_time = time.time()
solution01 = solution01(passports)
solution01_total_time = time.time() - solution01_start_time

solution02_start_time = time.time()
solution02 = solution02(passports)
solution02_total_time = time.time() - solution02_start_time

print("Solution 01:", solution01, "in", solution01_total_time)
print("Solution 02:", solution02, "in", solution02_total_time )

