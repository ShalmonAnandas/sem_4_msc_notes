class Sequence:
    def __init__(self, seq_id, seq_name):
        self.seq_id = seq_id
        self.seq_name = seq_name
        
class DNA(Sequence):
    def dna(self, protein):
        self.protein = protein
        print("DNA seq id: ", self.seq_id)
        print("DNA seq name: ", self.seq_name)
        print("DNA source: ", self.protein)

class RNA(Sequence):
    def rna(self, alphabet):
        self.alphabet = alphabet
        print("RNA seq id: ", self.seq_id)
        print("RNA seq name: ", self.seq_name)
        print("RNA alphabet: ", self.alphabet)

dna_obj = DNA(18273, "AOIWW")
dna_obj.dna("KERATIN")
print("\n")
rna_obj = RNA(12632, "RHSUI")
rna_obj.rna("RNA")
