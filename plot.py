from dna_utils import (
    count_bases, gc_content, reverse_complement, plot_base_counts,
    gc_content_sliding_window, plot_gc_content, translate_dna
)

# ✅ Your only DNA input
dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

# 🧬 Run all analysis
counts = count_bases(dna)
print("Base counts:", counts)

gc = gc_content(dna)
print("GC content (%):", gc)

rev_comp = reverse_complement(dna)
print("Reverse complement:", rev_comp)

protein = translate_dna(dna)
print("Protein:", protein)

# 📊 Visuals
plot_base_counts(counts)

gc_values = gc_content_sliding_window(dna, window_size=10)
plot_gc_content(gc_values)
