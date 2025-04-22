# JellyK at SemEval-2025 Task 11: Russian Multi-label Emotion Detection with Pre-trained BERT-based Language Models

This repository provides the code for our system, which achieved 4-th place at SemEval-2025 Task 11 track A (Russian subtask).

## Task: SemEval-2025 Task 11 track A
- Given a target text snippet, predict the perceived emotion(s) of the speaker. Specifically, select whether each of the following emotions apply: joy, sadness, fear, anger, surprise, or disgust. In other words, label the text snippet with: joy (1) or no joy (0), sadness (1) or no sadness (0), anger (1) or no anger (0), surprise (1) or no surprise (0), and disgust (1) or no disgust (0).
- For more details about the task and dataset, please refer to [the shared task paper](https://arxiv.org/abs/2503.07269).

## Method

## How to run

### Installation
```bash
git clone github.com/LeNguyenAnhKhoa/Russian-Emotion-Detection.git
cd Russian-Emotion-Detection
pip install -r requirements.txt
```

### AVeriTeC Data Preparation
Download the dataset and place it in the `Data` directory. You can found the dataset at [github.com/emotion-analysis-project/SemEval2025-task11](https://github.com/emotion-analysis-project/SemEval2025-Task11/tree/main/task-dataset/semeval-2025-task11-dataset/track_a)

### Configuration
Change the `model` or `batch_size` or everything you want in file `config.json`. Our default config:
```json
"batch_size": 64,
"train_path": "./Data/train/rus.csv",
"test_path": "./Data/test/rus.csv",
"learning_rate": 1e-5,
"base_model": "ai-forever/ruRoberta-large",
"num_labels": 6,
"problem_type": "multi_label_classification",
"LABELS": ["Anger", "Disgust", "Fear", "Joy", "Sadness", "Surprise"],
"num_epoch": 100,
"eps": 1e-9,
"th": 0.43,
"random_state": 2009,
"n_splits": 30,
"Min_loss": 0.08,
"num_fold": 10
```

### K-Fold Cross-Validation
Run all cells in file `kfold.ipynb`. You can analyze the error when showing `wrong_predict`.

### Final training and prediction
```python3
python main.py
```