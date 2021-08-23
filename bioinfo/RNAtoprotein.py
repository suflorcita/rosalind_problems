data_path = "bioinfo/rosalind_prot.txt"

from Bio.Seq import Seq

RNA = Seq(open(data_path).read())
print(RNA.translate())


