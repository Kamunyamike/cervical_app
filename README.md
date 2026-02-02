# cervical_app
Cervical Cancer Cell Classification (ResNet50)
This project implements a deep learning pipeline for cervical cancer cell classification using ResNet50. The model is trained on the SipakMed dataset, which contains five classes of cervical cell images:
Dyskeratotic
Koilocytotic
Metaplastic
Parabasal
Superficial-Intermediate
The goal is to provide an accurate, explainable, and reproducible tool for medical image classification, with deployment via Streamlit Cloud for easy access.
Features:
ResNet50 backbone with transfer learning for higher accuracy.
Data augmentation (rotation, flips, stain jitter, Gaussian blur) to improve generalization.
Training pipeline with checkpointing, early stopping, and learning rate scheduling.
Evaluation metrics: confusion matrix, classification report, and accuracy/loss curves.
Grad-CAM visualization for explainability (optional extension).
Streamlit webapp for interactive image upload and classification.
