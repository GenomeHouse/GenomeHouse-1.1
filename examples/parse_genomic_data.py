from genomehouse import genomic_parsers

for header, sequence in genomic_parsers.parse_fasta("example.fasta"):
    print(header, sequence)
