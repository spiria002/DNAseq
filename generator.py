import random

def generate_dna(length=5000):
    return ''.join(random.choices("ATGC", k=length))

# Example usage
long_seq = generate_dna(5000)
print(long_seq)

with open("data/synthetic_5000bp.fasta", "w") as f:
    f.write(">synthetic_5000bp_sequence\n")
    for i in range(0, len(long_seq), 80):
        f.write(long_seq[i:i+80] + "\n")
