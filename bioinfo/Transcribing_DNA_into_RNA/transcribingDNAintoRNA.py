
def main(): 
    path = "rosalind_rna.txt"

    DNA = open(path).read()
    print(DNA.replace("T", "U"))

if __name__ == "__main__":
    main()

