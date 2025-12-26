import streamlit as st
import sys
import os

# srcディレクトリをパスに追加してモジュールインポートを解決
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.learning import content, quiz
from src.training import model_loader, trainer
from src.utils import helpers

st.set_page_config(
    page_title="LLM Learning App",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("📚 LLM Learning & Creation Studio")
    
    # 状態管理の初期化
    if 'current_model' not in st.session_state:
        st.session_state.current_model = None
    if 'current_tokenizer' not in st.session_state:
        st.session_state.current_tokenizer = None
        
    # サイドバーでモード選択
    mode = st.sidebar.selectbox(
        "モード選択",
        ["学習モード", "トレーニングモード"]
    )
    
    if mode == "学習モード":
        render_learning_mode()
    else:
        render_training_mode()

def render_learning_mode():
    st.header("📝 コンセプト学習")
    
    topics = content.get_all_topics()
    selected_topic_id = st.sidebar.radio(
        "トピック",
        list(topics.keys()),
        format_func=lambda x: topics[x]['title']
    )
    
    topic_data = content.get_topic(selected_topic_id)
    
    # コンテンツ表示
    st.markdown(topic_data['content'])
    
    st.divider()
    
    # クイズ表示
    st.subheader("理解度チェッククイズ")
    quizzes = quiz.get_quiz_for_topic(selected_topic_id)
    
    for i, q in enumerate(quizzes):
        st.write(f"**Q{i+1}. {q['question']}**")
        answer = st.radio(
            "選択してください:",
            q['options'],
            key=f"quiz_{selected_topic_id}_{i}"
        )
        
        if st.button("回答する", key=f"btn_{selected_topic_id}_{i}"):
            if q['options'].index(answer) == q['answer']:
                st.success("正解！ " + q['explanation'])
            else:
                st.error("不正解です。")

def render_training_mode():
    st.header("🛠️ モデルトレーニング実践")
    
    st.info("このモードでは、実際にGPT-2モデルをロードしてファインチューニングを体験できます。")
    
    # モデルロードセクション
    st.subheader("1. モデルの準備")
    if st.button("ベースモデル(GPT-2)をロード"):
        with st.spinner("モデルをダウンロード中...（初回は時間がかかります）"):
            tokenizer, model = model_loader.load_model()
            if model and tokenizer:
                st.session_state.current_model = model
                st.session_state.current_tokenizer = tokenizer
                st.success("モデルのロードが完了しました！")
            else:
                st.error("モデルのロードに失敗しました。")
                
    if st.session_state.current_model:
        st.write("✅ モデルロード済み")
        
        # データ入力セクション
        st.subheader("2. 学習データ")
        input_text = st.text_area(
            "学習させたいテキストを入力してください:",
            height=150,
            value="AIは未来の技術です。\nディープラーニングはAIの一分野です。\n機械学習はデータから学びます。"
        )
        
        # トレーニングセクション
        st.subheader("3. ファインチューニング")
        epochs = st.slider("エポック数 (繰り返し回数)", 1, 5, 1)
        
        if st.button("学習開始"):
            texts = [line for line in input_text.split('\n') if line.strip()]
            if not texts:
                st.warning("テキストを入力してください。")
            else:
                with st.spinner(f"{epochs}エポックで学習中..."):
                    # トレーニング実行
                    model, losses = trainer.train_model(
                        st.session_state.current_model,
                        st.session_state.current_tokenizer,
                        texts,
                        epochs=epochs
                    )
                    
                    st.success("学習完了！")
                    st.line_chart(losses)
                    st.session_state.current_model = model
        
        # 生成テストセクション
        st.subheader("4. 動作確認")
        prompt = st.text_input("プロンプト（書き出し）:", "AIは")
        
        if st.button("テキスト生成"):
            generated = model_loader.generate_text(
                st.session_state.current_model,
                st.session_state.current_tokenizer,
                prompt
            )
            st.write("### 生成結果:")
            st.write(generated)

if __name__ == "__main__":
    main()
