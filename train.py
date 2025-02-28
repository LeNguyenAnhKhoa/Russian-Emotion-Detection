import gc, torch
from sklearn.metrics import f1_score
import numpy as np

def cleanup():
    gc.collect()
    torch.cuda.empty_cache()

def train(num_epoch, model, train_loader, valid_loader, optimizer, th, Min_valid):
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model = model.to(device)
    train_losses = []
    valid_losses = []
    train_f1scores = []
    valid_f1scores = []
    for epoch in range(num_epoch):
        train_loss = 0
        valid_loss = 0
        train_f1score = 0
        valid_f1score = 0
        model.train()
        for i, batch in enumerate(train_loader):
            batch = {k: v.to(device) for k, v in batch.items() if k != "text"}
            outputs = model(**batch)
            logits = outputs.logits
            predictions = np.array(torch.sigmoid(logits).tolist())
            predictions = np.where(predictions > th, 1, 0)
            label = batch["labels"].cpu().numpy()
            train_f1score = train_f1score + f1_score(label, predictions, average='macro', zero_division=1)
            train_loss = train_loss + outputs.loss
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
        model.eval()
        for batch in valid_loader:
            batch = {k: v.to(device) for k, v in batch.items() if k != "text"}
            with torch.no_grad():
                outputs = model(**batch)
            logits = outputs.logits
            predictions = np.array(torch.sigmoid(logits).tolist())
            predictions = np.where(predictions > th, 1, 0)
            label = batch["labels"].cpu().numpy()
            valid_f1score = valid_f1score + f1_score(label, predictions, average='macro', zero_division=1)
            valid_loss = valid_loss + outputs.loss
        cleanup()
        cleanup()
        cleanup()
        train_loss = (train_loss/len(train_loader)).item()
        valid_loss = (valid_loss/len(valid_loader)).item()
        train_f1score = (train_f1score/len(train_loader)).item()
        valid_f1score = (valid_f1score/len(valid_loader)).item()
        print(f"Epoch {epoch+1} - Loss: {train_loss:.3f} - F1-score: {train_f1score:.3f} - val_loss: {valid_loss:.3f} - valid-F1-score: {valid_f1score:.3f}")   
        train_losses.append(train_loss)
        valid_losses.append(valid_loss)
        train_f1scores.append(train_f1score)
        valid_f1scores.append(valid_f1score)
        if train_loss < 0.08 or valid_loss < Min_valid:
            break
    return model, train_losses, valid_losses, train_f1scores, valid_f1scores