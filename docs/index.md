# GenomeHouse Documentation

Welcome to GenomeHouse, a modular Python toolkit for bioinformatics.

## Features
- Sequence analysis (reverse complement, motif search, GC content, translation)
- Genomic data parsing (FASTA, FASTQ, VCF, GFF/GTF)
- Machine learning pipelines for biological data
- Publication-quality data visualization
- Statistical analysis tools
- Extensible and user-friendly API

## Quick Start
```bash
pip install genomehouse
```

## Example Usage
```python
from genomehouse import sequence_tools, genomic_parsers
seq = "ATGCGTAC"
print(sequence_tools.gc_content(seq))
for header, seq in genomic_parsers.parse_fasta("example.fasta"):
    print(header, seq)
```

See `usage_examples.md` for more details and advanced workflows.
