
QUIZ_DATA = {
    "llm_basics": [
        {
            "question": "LLMは何の略ですか？",
            "options": ["Large Language Model", "Long Learning Machine", "Little Logic Module"],
            "answer": 0,
            "explanation": "LLMは Large Language Model（大規模言語モデル）の略です。"
        },
        {
            "question": "LLMの主な学習方法は？",
            "options": ["画像認識", "次に来る単語の予測", "音声合成"],
            "answer": 1,
            "explanation": "LLMは主に、文脈から「次に来る単語」を予測するように事前学習されます。"
        }
    ],
    "transformer": [
        {
            "question": "Transformerの核となる機構は？",
            "options": ["Convolution", "Self-Attention", "Backpropagation"],
            "answer": 1,
            "explanation": "Self-Attention（自己注意機構）がTransformerのキーとなる技術です。"
        }
    ],
    "tokenization": [
        {
            "question": "「サブワード」トークナイゼーションの利点は？",
            "options": ["処理が遅い", "未知語への対応力が高い", "単語数が減る"],
            "answer": 1,
            "explanation": "頻出する単語はそのまま、珍しい単語は分割することで、未知語にも柔軟に対応できます。"
        }
    ],
    "transfer_learning": [
        {
            "question": "事前学習済みモデルを特定のタスクに適応させることを何と言いますか？",
            "options": ["プリトレーニング", "スクラッチ学習", "ファインチューニング"],
            "answer": 2,
            "explanation": "既存の知識（事前学習）を特定タスクに微調整することをファインチューニングと言います。"
        }
    ],
    "fine_tuning": [
        {
            "question": "ファインチューニング時の学習率は一般的にどう設定しますか？",
            "options": ["事前学習時より低くする", "事前学習時より高くする", "ランダムにする"],
            "answer": 0,
            "explanation": "せっかく学習した知識を壊さないよう、低い学習率で慎重に重みを更新します。"
        }
    ]
}

def get_quiz_for_topic(topic_id):
    return QUIZ_DATA.get(topic_id, [])
