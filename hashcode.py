with open("small.in", "r") as input_file:
	first_line = input_file.readline()
	whole = input_file.read()
first_arr = first_line.split()
arr = [[0 for i in range(int(first_arr[0]))] for j in range(int(first_arr[1]))]
print whole.split()