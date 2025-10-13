# 🧮 Dataset - AI Text Detection

This folder contains a **reduced version** of the original dataset used for model training.

- **Source:** [AI vs Human Text Dataset – Kaggle](https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text)
- **Original size:** ~ 1 GB
- **Reduced version:** ~ 44 MB
- **Structure:**
  - `text` → the content of the text
  - `label` → 0 = Human, 1 = AI

### ⚙️ How this subset was created
A random, balanced subset of 10,000 samples per class was selected to make the project reproducible on GitHub without exceeding file limits.

You can download the **full dataset** from Kaggle if you wish to retrain the models completely.