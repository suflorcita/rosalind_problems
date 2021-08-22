data_path = "C:/Users/Sol/projects/Rosalinda/py_basics/rosalind_ini5.txt"


file = open(data_path, 'r')
i = 0 

for line in file: 
    if i % 2 != 0:
        print(line.strip())
    i += 1
