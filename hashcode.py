def read_file(title):
	with open(title, "r") as input_file:
		first_line = input_file.readline()
		whole = input_file.read()
	first_arr = first_line.split()
	arr = [[0 for i in range(int(first_arr[1]))] for j in range(int(first_arr[0]))]
	whole_arr = whole.split()
	j_count = 0
	i_count = 0
	for i in whole_arr:
		for j in i:
			arr[i_count-1][j_count-1] = j
			j_count += 1
		j_count = 0
		i_count += 1
	return arr

pizza = read_file("small.in")
arr = [[0 for i in range(len(pizza[0]))] for j in range(len(pizza))]
j_count = 0
i_count = 0
for i in pizza:
	pass
	for j in i:
		pass
