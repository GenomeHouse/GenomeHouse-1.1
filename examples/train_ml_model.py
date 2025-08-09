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
