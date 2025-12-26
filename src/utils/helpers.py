import os

def save_model_artifact(model, tokenizer, path="models/my_model"):
    """
    モデルを保存するためのヘルパー関数
    """
    try:
        os.makedirs(path, exist_ok=True)
        model.save_pretrained(path)
        tokenizer.save_pretrained(path)
        return True
    except Exception as e:
        print(f"Error saving model: {e}")
        return False
