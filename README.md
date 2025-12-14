# LLM学習用アプリケーション

学びながら自分のLLMモデルを作成できるインタラクティブな学習アプリケーション

## 🎯 コンセプト

このアプリケーションは、LLM（大規模言語モデル）について学びながら、実際に自分のモデルを作成できる教育用プラットフォームです。

### 主な特徴

1. **学習フェーズ**: LLMの基礎知識をインタラクティブに学習
2. **実践フェーズ**: Hugging Faceのオープンソースモデルを使った転移学習
3. **ハンズオン**: 実際にモデルをファインチューニングして、テキスト生成を体験

## 📋 必要要件

- Python 3.9以上
- pip

### 推奨環境
- GPU搭載マシン（オプション、学習を高速化）
- 8GB以上のRAM

## 🚀 セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/Wataru-kashiwa/llm-learning-app.git
cd llm-learning-app
```

### 2. 仮想環境の作成（推奨）

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

### 3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

## 💡 使い方

### アプリケーションの起動

```bash
streamlit run src/app.py
```

ブラウザが自動的に開き、アプリケーションが表示されます（通常は http://localhost:8501）。

### 学習の流れ

#### Phase 1: 基礎知識の学習
1. サイドバーから「学習モード」を選択
2. 5つのトピックを順番に学習
3. 各トピック後のクイズで理解度をチェック

#### Phase 2: モデルの作成
1. 「トレーニングモード」を選択
2. サンプルデータまたは独自データをアップロード
3. ハイパーパラメータを設定
4. ファインチューニングを実行
5. 作成したモデルでテキスト生成を試す

## 📚 学習トピック

1. **LLMとは**: 大規模言語モデルの基本概念
2. **Transformerアーキテクチャ**: 注意機構とエンコーダー・デコーダー
3. **トークナイゼーション**: テキストをトークンに分割する方法
4. **転移学習**: 事前学習済みモデルの活用
5. **ファインチューニング**: モデルのカスタマイズ

## 🧪 テストの実行

```bash
# 全テストを実行
pytest

# カバレッジ付きでテストを実行
pytest --cov=src tests/

# 特定のテストファイルを実行
pytest tests/test_learning.py
```

## 📁 プロジェクト構造

```
llm-learning-app/
├── src/
│   ├── learning/          # 学習コンテンツモジュール
│   │   ├── __init__.py
│   │   ├── content.py     # 学習コンテンツ
│   │   └── quiz.py        # クイズ機能
│   ├── training/          # モデルトレーニングモジュール
│   │   ├── __init__.py
│   │   ├── model_loader.py    # モデルローダー
│   │   ├── trainer.py         # トレーニング機能
│   │   └── data_processor.py  # データ処理
│   ├── utils/             # ユーティリティ
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── app.py             # メインアプリケーション
├── tests/                 # テストコード
│   ├── __init__.py
│   ├── test_learning.py
│   ├── test_training.py
│   └── test_utils.py
├── data/                  # サンプルデータ
│   └── sample_texts.txt
├── models/                # 保存されたモデル
├── requirements.txt       # 依存パッケージ
├── README.md             # このファイル
└── plan.md               # 開発計画
```

## 🔧 使用技術

- **Hugging Face Transformers**: モデルのロードとファインチューニング
- **Streamlit**: インタラクティブなWebアプリケーション
- **PyTorch**: 深層学習フレームワーク
- **pytest**: テストフレームワーク

## 📝 開発について

### TDD（テスト駆動開発）
このプロジェクトではTDDを採用しています：
- 新機能追加前に必ずテストを作成
- 各モジュールに対応するテストファイルが存在
- カバレッジ80%以上を目標

### 開発の流れ
詳細な開発計画と進捗は[plan.md](plan.md)を参照してください。

## 🤝 コントリビューション

プルリクエストを歓迎します！大きな変更の場合は、まずissueを開いて変更内容を議論してください。

## 📄 ライセンス

MIT License

## 🙏 謝辞

- [Hugging Face](https://huggingface.co/) - オープンソースモデルとライブラリの提供
- [Streamlit](https://streamlit.io/) - 素晴らしいWebフレームワーク

## ⚠️ 注意事項

- このアプリケーションは教育目的で作成されています
- 大規模なモデルをトレーニングする場合は、十分なコンピューティングリソースが必要です
- 初回実行時にモデルのダウンロードが行われるため、時間がかかる場合があります

## 📧 お問い合わせ

問題や質問がある場合は、GitHubのIssuesでお知らせください。
