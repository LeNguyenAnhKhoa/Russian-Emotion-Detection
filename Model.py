from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertForSequenceClassification

class Model:
    def __init__(self, base_model, num_labels, problem_type, LABELS):
        self.tokenizer = AutoTokenizer.from_pretrained(base_model)
        self.model = AutoModelForSequenceClassification.from_pretrained(base_model, num_labels=num_labels, problem_type=problem_type)
        self.model.config.label2id = {label: i for i, label in enumerate(LABELS)}
        self.model.config.id2label = {i: label for i, label in enumerate(LABELS)}

    def build(self):
        return self.model, self.tokenizer