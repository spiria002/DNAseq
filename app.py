import streamlit as st
from dna_utils import (
    count_bases, gc_content, reverse_complement, translate_dna,
    plot_base_counts, codon_usage, plot_codon_usage
)

st.title("🧬 DNAseq Bioinformatics App")

st.markdown("Paste a DNA sequence below (ATGC only):")

user_input = st.text_area("DNA Sequence", height=150)

if user_input:
    seq = user_input.upper().replace("\n", "").replace(" ", "")

    if len(seq) > 5000:
        st.warning("⚠️ Sequence too long! Please paste a sequence under 5000 bases.")
    else:
        with st.spinner("Analysing sequence..."):

            # --- Base counts ---
            st.subheader("🧬 Base Counts")
            counts = count_bases(seq)
            st.write(counts)

            if st.checkbox("Show base count plot"):
                plot_base_counts(counts)

            # --- GC content ---
            st.subheader("📊 GC Content")
            st.write(f"{gc_content(seq)} %")

            # --- Reverse complement ---
            st.subheader("🔁 Reverse Complement")
            st.write(reverse_complement(seq))

            # --- Protein translation ---
            st.subheader("🧫 Translated Protein")
            st.write(translate_dna(seq))

            # --- Codon usage ---
            st.subheader("📈 Codon Usage (Top 10)")
            codons = codon_usage(seq)
            plot_codon_usage(codons, top_n=10)
