
def main(): 
    path = "rosalind_revc.txt"
    DNA = open(path).read()
    reverseDNA =  DNA[::-1]

    print(reverseDNA.translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G':'C'})))

if __name__ == '__main__':
    main()
