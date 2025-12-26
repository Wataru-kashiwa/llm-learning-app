import torch
from torch.utils.data import DataLoader
from torch.optim import AdamW
from .data_processor import TextDataset

def train_model(model, tokenizer, texts, epochs=1, batch_size=4, learning_rate=5e-5):
    """
    非常にシンプルなトレーニングループ。
    最低限のファインチューニング機能を提供。
    """
    dataset = TextDataset(tokenizer, texts)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    optimizer = AdamW(model.parameters(), lr=learning_rate)
    
    model.train()
    losses = []
    
    for epoch in range(epochs):
        epoch_loss = 0
        for batch in loader:
            optimizer.zero_grad()
            
            input_ids = batch['input_ids']
            attention_mask = batch['attention_mask']
            labels = batch['labels']
            
            outputs = model(
                input_ids=input_ids, 
                attention_mask=attention_mask, 
                labels=labels
            )
            
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item()
        
        avg_loss = epoch_loss / len(loader)
        losses.append(avg_loss)
        print(f"Epoch {epoch+1}/{epochs}, Loss: {avg_loss}")
        
    return model, losses
