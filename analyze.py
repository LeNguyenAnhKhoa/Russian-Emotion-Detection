import torch
import numpy as np
import pandas as pd

def show_different_emotions(row):
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']
    different_emotions = []
    
    for i, (pred, lab) in enumerate(zip(row['predict'], row['label'])):
        if pred != lab:
            different_emotions.append(f"{emotions[i]}: predict={pred}, label={lab}")
    
    return different_emotions if different_emotions else None

def analyze(model, valid_loader, th):
    wrong_predictions = []
    model.eval()
    
    for batch in valid_loader:
        texts = batch["text"]
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        batch = {k: v.to(device) for k, v in batch.items() if k != "text"}
        with torch.no_grad():
            outputs = model(**batch)
        logits = outputs.logits
        predictions = np.array(torch.sigmoid(logits).tolist())
        predictions = np.where(predictions > th, 1, 0)
        labels = batch["labels"].cpu().numpy().astype(int) 

        for i in range(len(labels)):
            if not np.array_equal(predictions[i], labels[i]):
                wrong_predictions.append({
                    "text": texts[i], 
                    "predict": predictions[i].tolist(),
                    "label": labels[i].tolist()
                })

    result = pd.DataFrame(wrong_predictions)
    result['different_emotions'] = result.apply(show_different_emotions, axis=1)
    result = result[result['different_emotions'].notna()]

    return result[['text', 'different_emotions']]
