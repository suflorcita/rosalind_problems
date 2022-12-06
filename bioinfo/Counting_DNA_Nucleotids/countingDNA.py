
def main(): 
    data_path = "rosalind_dna_2_dataset.txt"

    DNA = open(data_path).read()
        
    print(DNA.count("A"),
    DNA.count("G"),
    DNA.count("C"),
    DNA.count("T"))


if __name__ == "__main__":
    main()

