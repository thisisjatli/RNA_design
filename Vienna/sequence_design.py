import os
import pickle
from ViennaRNA import RNA
from Bio import SeqIO

def get_seq_from_fasta(fasta_file):
# Read the FASTA file and extract the sequence
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = record.seq
        print(f"Sequence ID: {record.id}")
        print(f"Sequence: {sequence}")
    return str(sequence)

free_energy = {}
for fasta_file in os.listdir('../Rosetta/raw_test'):
    if not fasta_file.endswith('.fasta'):
        continue
    
    # RNA sequence
    sequence = get_seq_from_fasta(f'../Rosetta/raw_test/{fasta_file}')

    # Predict the secondary structure (dot-bracket notation)
    structure, mfe = RNA.fold(sequence)

    
    basename, ext = os.path.splitext(fasta_file)
    free_energy[basename] = mfe
    # with open(f'ss_predictions/{basename}.in', 'w') as fr:
    #     fr.write(structure)

    print("RNA Sequence:", sequence)
    print("Predicted Structure:", structure)
    print("Minimum Free Energy:", mfe)

with open('minimum_free_energy.pkl', 'wb') as fw:
    pickle.dump(free_energy, fw)
