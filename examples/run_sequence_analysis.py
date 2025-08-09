from genomehouse import sequence_tools

seq = "ATGCGTAC"
print("Reverse complement:", sequence_tools.reverse_complement(seq))
print("GC content:", sequence_tools.gc_content(seq))
print("Motif positions:", sequence_tools.find_motif(seq, "CG"))
print("Protein translation:", sequence_tools.translate(seq))
