''''''

data_path = "py_basics/rosalind_ini2.txt"

def square_hyp(num1, num2): 
    return num1 ** 2 + num2 ** 2

numbers = open(data_path).read()
numbers = list(map(int, numbers.split()))

print(square_hyp(numbers[0], numbers[1]))
