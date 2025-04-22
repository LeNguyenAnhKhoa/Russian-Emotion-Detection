import json, torch
from LoadData import load_dataset
from Model import Model
from EmotionDataset import EmotionDataset
from train import train
from plot import plot
from predict import predict
from sklearn.model_selection import KFold
import numpy as np
from analyze import analyze

with open("./config.json", "r") as file:
    config = json.load(file)
batch_size = config["batch_size"]
train_path = config["train_path"]
test_path = config["test_path"]
learning_rate = config["learning_rate"]
base_model = config["base_model"]
num_labels = config["num_labels"]
problem_type = config["problem_type"]
labels = config["LABELS"]
num_epoch = config["num_epoch"]
eps = config["eps"]
th = config["th"]
random_state = config["random_state"]
n_splits = config["n_splits"]
Min_loss = config["Min_loss"]
num_folds = config["num_fold"]

X_train, y_train, X_test, test_df = load_dataset(train_path, test_path)
X_train, y_train = X_train.tolist(), y_train.tolist()
model, tokenizer = Model(base_model, num_labels, problem_type, labels).build()
train_loader, test_loader = EmotionDataset(tokenizer, batch_size).build_dataset(X_train, y_train, X_test)
optimizer = torch.optim.AdamW(model.parameters(), lr = learning_rate, betas = (0.9, 0.98), eps = eps, weight_decay=0.01)
model = train(num_epoch, model, train_loader, optimizer, th, Min_loss)
predict(model, test_loader, test_df, th)
