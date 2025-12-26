import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model(model_name="gpt2"):
    """
    モデルとトークナイザーをロードします。
    教育用のため、デフォルトは軽量なgpt2を使用します。
    """
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        
        # パディングトークンの設定（GPT-2用）
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            
        return tokenizer, model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None

def generate_text(model, tokenizer, prompt, max_length=50):
    """
    テキスト生成のデモ用関数
    """
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # 簡略化のためCPU実行を想定
    with torch.no_grad():
        outputs = model.generate(
            **inputs, 
            max_length=max_length, 
            do_sample=True, 
            temperature=0.7,
            pad_token_id=tokenizer.pad_token_id
        )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
