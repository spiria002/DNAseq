import matplotlib.pyplot as plt
import streamlit as st  # Add this line

# 🧬 Count DNA bases
def count_bases(seq):
    seq = seq.upper()
    counts = {base: seq.count(base) for base in "ATGC"}

    valid_bases = set("ATGC")
    found_bases = set(seq)
    invalid_bases = found_bases - valid_bases

    if invalid_bases:
        print(f"⚠️ Warning: Sequence contains invalid characters: {', '.join(invalid_bases)}")

    return counts

# 📈 GC content %
def gc_content(seq):
    seq = seq.upper()
    gc = seq.count('G') + seq.count('C')
    return round((gc / len(seq)) * 100, 2)

# 🔁 Reverse complement
def reverse_complement(seq):
    seq = seq.upper()
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    rev_comp = ''.join([complement.get(base, 'N') for base in reversed(seq)])
    return rev_comp


def plot_base_counts(counts, title="DNA Base Counts"):
    bases = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(6, 4))
    plt.bar(bases, values)
    plt.title(title)
    plt.xlabel("Base")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    st.pyplot(plt)  # ✅ this tells Streamlit to display the plot


# 📈 GC content over sliding window
def gc_content_sliding_window(seq, window_size=10):
    seq = seq.upper()
    gc_values = []

    for i in range(0, len(seq) - window_size + 1):
        window = seq[i:i+window_size]
        gc = (window.count("G") + window.count("C")) / window_size
        gc_values.append(round(gc * 100, 2))

    return gc_values

# 📉 Plot sliding window GC content
def plot_gc_content(gc_values, window_size=10):
    positions = list(range(len(gc_values)))

    plt.figure(figsize=(10, 4))
    plt.plot(positions, gc_values, marker='o', linestyle='-', linewidth=1)
    plt.title(f'GC Content (Window Size = {window_size})')
    plt.xlabel("Window Start Position")
    plt.ylabel("GC Content (%)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

# 🔣 Codon dictionary
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

# 🧬 Translate DNA to protein
def translate_dna(seq):
    seq = seq.upper()
    protein = ""

    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        amino_acid = codon_table.get(codon, 'X')
        if amino_acid == '_':
            break
        protein += amino_acid

    return protein

def load_fasta(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        seq = ''.join(line.strip() for line in lines if not line.startswith(">"))
    return seq

def codon_usage(seq):
    seq = seq.upper()
    codon_counts = {}

    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if len(codon) == 3:
            codon_counts[codon] = codon_counts.get(codon, 0) + 1

    return codon_counts

def plot_codon_usage(codon_counts, top_n=10):
    sorted_codons = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    codons, counts = zip(*sorted_codons)

    plt.figure(figsize=(10, 4))
    plt.bar(codons, counts)
    plt.title(f"Top {top_n} Codons by Frequency")
    plt.xlabel("Codon")
    plt.ylabel("Count")
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    st.pyplot(plt)  # ✅ show the plot in Streamlit

