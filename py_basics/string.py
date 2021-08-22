data_path = "py_basics/rosalind_ini3.txt"


file = open(data_path, 'r')
string = file.readline()

positions = list(map(int, file.readline().split()))

print(string[positions[0]:positions[1] + 1] + ' ' + string[positions[2]:positions[3] + 1])

