from dna_utils import (
    count_bases, gc_content, reverse_complement, plot_base_counts,
    gc_content_sliding_window, plot_gc_content, translate_dna,
    load_fasta, codon_usage, plot_codon_usage
)

# --- Load DNA from FASTA file ---
fasta_dna = load_fasta("data/tp53.fasta")
print("📄 FASTA DNA loaded.")

# --- DNA Summary ---
print("Base counts:", count_bases(fasta_dna))
print("GC content (%):", gc_content(fasta_dna))
print("Reverse complement:", reverse_complement(fasta_dna))
print("Protein:", translate_dna(fasta_dna))

# --- Plots ---
plot_base_counts(count_bases(fasta_dna), title="Base Counts")
plot_gc_content(gc_content_sliding_window(fasta_dna, window_size=10), window_size=10)
plot_codon_usage(codon_usage(fasta_dna), top_n=10)

