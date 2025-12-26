import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# srcディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.utils import helpers

class TestUtils(unittest.TestCase):
    @patch('src.utils.helpers.os.makedirs')
    def test_save_model(self, mock_makedirs):
        model = MagicMock()
        tokenizer = MagicMock()
        
        result = helpers.save_model_artifact(model, tokenizer, "test_path")
        
        self.assertTrue(result)
        model.save_pretrained.assert_called_with("test_path")
        tokenizer.save_pretrained.assert_called_with("test_path")

if __name__ == '__main__':
    unittest.main()
