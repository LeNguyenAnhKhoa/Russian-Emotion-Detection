import torch
import numpy as np
import pandas as pd

def predict(model, test_loader, test_df, th):
    model.eval()
    pred = []
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    for batch in test_loader:
        batch = {k: v.to(device) for k, v in batch.items() if k != "text"}
        with torch.no_grad():
            outputs = model(**batch)
        logits = outputs.logits
        predictions = np.array(torch.sigmoid(logits).tolist())
        predictions = np.where(predictions > th, 1, 0)
        for i in predictions:
            pred.append(i)
    
    sub = test_df.copy()
    sub = sub.drop(['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'text'], axis = 1)
    sub['label'] = pred
    sub[['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']] = pd.DataFrame(sub['label'].tolist(), index=sub.index)
    sub = sub.drop(['label'], axis = 1)
    sub.to_csv("submission.csv", index=False)
