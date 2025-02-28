from TextDataset import TextDataset
from torch.utils.data import DataLoader

class EmotionDataset:
    def __init__(self, tokenizer, batch_size=64):
        self.tokenizer = tokenizer
        self.batch_size = batch_size

    def build_dataset(self, X_train, y_train, X_valid, y_valid, X_test, padding=True, truncation=True, max_length=128):
        train_encoding = self.tokenizer(
            X_train,
            padding=padding,
            truncation=truncation,
            max_length=max_length
        )
        valid_encoding = self.tokenizer(
            X_valid, 
            padding=padding,
            truncation=truncation,
            max_length=max_length
        )
        test_encoding = self.tokenizer(
            X_test,
            padding=True,
            truncation=True,
            max_length=max_length
        )

        train_encoding["text"] = X_train
        valid_encoding["text"] = X_valid    
        test_encoding["text"] = X_test

        train_dataset = TextDataset(train_encoding, y_train)
        valid_dataset = TextDataset(valid_encoding, y_valid)
        test_dataset = TextDataset(test_encoding)

        train_loader = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True)
        valid_loader = DataLoader(valid_dataset, batch_size=self.batch_size)
        test_loader = DataLoader(test_dataset, batch_size=self.batch_size)

        return train_loader, valid_loader, test_loader
