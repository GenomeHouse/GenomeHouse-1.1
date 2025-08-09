# GenomeHouse Usage Examples

## Sequence Analysis
```python
from genomehouse import sequence_tools
seq = "ATGCGTAC"
print("Reverse complement:", sequence_tools.reverse_complement(seq))
print("GC content:", sequence_tools.gc_content(seq))
print("Motif positions:", sequence_tools.find_motif(seq, "CG"))
print("Protein translation:", sequence_tools.translate(seq))
```

## Genomic Data Parsing
```python
from genomehouse import genomic_parsers
for header, sequence in genomic_parsers.parse_fasta("example.fasta"):
    print(header, sequence)
```

## Machine Learning Workflow
```python
from genomehouse import ml_models
import numpy as np
sequences = ["ATGCGA", "TTAGGC", "GGCCAA"]
labels = [1, 0, 1]
features = ml_models.extract_features(sequences)
X = np.array(features)
y = np.array(labels)
model, acc, report = ml_models.train_classifier(X, y)
print("Accuracy:", acc)
print(report)
ml_models.save_model(model, "rf_model.joblib")
```

## Visualization
```python
from genomehouse import visualization
visualization.plot_gc_distribution([40, 50, 60, 55, 45, 70])
```
