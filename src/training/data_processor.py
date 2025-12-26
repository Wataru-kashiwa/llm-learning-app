from torch.utils.data import Dataset

class TextDataset(Dataset):
    def __init__(self, tokenizer, texts, block_size=128):
        self.examples = []
        
        # 非常にシンプルなデータセット作成
        for text in texts:
            tokenized = tokenizer(
                text, 
                truncation=True, 
                max_length=block_size, 
                padding="max_length"
            )
            self.examples.append(tokenized)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, i):
        item = {key: torch.tensor(val) for key, val in self.examples[i].items()}
        item["labels"] = item["input_ids"].clone()
        return item

import torch
