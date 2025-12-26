
TOPICS = {
    "llm_basics": {
        "title": "LLMとは",
        "content": """
## 大規模言語モデル (LLM) とは

LLM (Large Language Model) は、大量のテキストデータから学習し、人間のような文章を生成したり、理解したりできるAIモデルです。

### 主な特徴
- **大規模なパラメータ**: 数十億から数兆のパラメータを持ちます。
- **事前学習**: 大量のテキストデータを使って、「次に来る単語」を予測するように学習します。
- **汎用性**: 翻訳、要約、質問応答など、多様なタスクをこなせます。

### 代表的なモデル
- GPT-4 (OpenAI)
- Claude 3 (Anthropic)
- LLaMA (Meta)
"""
    },
    "transformer": {
        "title": "Transformerアーキテクチャ",
        "content": """
## Transformerアーキテクチャ

2017年にGoogleの研究者によって発表された「Attention Is All You Need」という論文で提案されたモデル構造です。

### 仕組み
- **Self-Attention (自己注意機構)**: 文脈の中でどの単語が重要かを計算します。
- **並列処理**: RNNと比較して、並列計算が得意で学習が高速です。
"""
    },
    "tokenization": {
        "title": "トークナイゼーション",
        "content": """
## トークナイゼーション

テキストをモデルが処理できる最小単位（トークン）に分割するプロセスです。

### 種類
- **単語単位**: apple, is, a, fruit
- **文字単位**: a, p, p, l, e
- **サブワード**: app, ##le (BPEなど)

現代のLLMは主にサブワード方式を採用しており、効率的に未知語に対応できます。
"""
    },
    "transfer_learning": {
        "title": "転移学習",
        "content": """
## 転移学習 (Transfer Learning)

あるタスクで学習した知識を、別のタスクに応用する手法です。

### LLMにおける流れ
1. **事前学習 (Pre-training)**: 大規模データで一般的な言語能力を習得
2. **ファインチューニング (Fine-tuning)**: 特定のタスクデータで再学習

これにより、少ないデータでも高性能なモデルを作ることができます。
"""
    },
    "fine_tuning": {
        "title": "ファインチューニング",
        "content": """
## ファインチューニング

事前学習済みモデルの重みを、特定のデータセットに合わせて微調整することです。

### 手順
1. 事前学習モデルをロード
2. カスタムデータセットを準備
3. 低い学習率で再学習
4. 特定のタスク（医療、法律、キャラ付けなど）に適応させる
"""
    }
}

def get_topic(topic_id):
    return TOPICS.get(topic_id)

def get_all_topics():
    return TOPICS
