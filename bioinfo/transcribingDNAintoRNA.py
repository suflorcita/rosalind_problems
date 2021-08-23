path = "C:/Users/Sol/projects/Rosalinda/bioinfo/rosalind_rna.txt"

DNA = open(path).read()
print(DNA.replace("T", "U"))