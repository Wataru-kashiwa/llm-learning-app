import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# srcディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.training import data_processor, trainer

class TestTraining(unittest.TestCase):
    def setUp(self):
        self.tokenizer = MagicMock()
        # トークナイザーの振る舞いをモック
        self.tokenizer.return_value = {
            "input_ids": [1, 2, 3],
            "attention_mask": [1, 1, 1]
        }
        self.tokenizer.pad_token_id = 0
        
    def test_dataset_creation(self):
        texts = ["Hello world", "Test sentence"]
        dataset = data_processor.TextDataset(self.tokenizer, texts)
        self.assertEqual(len(dataset), 2)
        
    @patch('src.training.trainer.DataLoader')
    @patch('src.training.trainer.AdamW')
    def test_train_loop(self, mock_optimizer, mock_loader):
        # 非常に簡易的なトレーニングループのテスト
        # 実際のトレーニングは時間がかかるためモックを使用
        model = MagicMock()
        model.parameters.return_value = []
        
        # DataLoaderのモック
        batch = {
            'input_ids': MagicMock(),
            'attention_mask': MagicMock(),
            'labels': MagicMock()
        }
        mock_loader.return_value = [batch]
        
        # モデル出力のモック
        outputs = MagicMock()
        outputs.loss = MagicMock()
        outputs.loss.item.return_value = 0.5
        model.return_value = outputs
        
        texts = ["test"]
        model, losses = trainer.train_model(model, self.tokenizer, texts, epochs=1)
        
        self.assertEqual(len(losses), 1)
        self.assertEqual(losses[0], 0.5)

if __name__ == '__main__':
    unittest.main()
