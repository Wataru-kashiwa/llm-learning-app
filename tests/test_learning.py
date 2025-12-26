import os
import sys

# srcディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.learning import content, quiz

def test_get_all_topics():
    topics = content.get_all_topics()
    assert len(topics) == 5
    assert "llm_basics" in topics

def test_get_topic_content():
    topic = content.get_topic("llm_basics")
    assert topic is not None
    assert "title" in topic
    assert "content" in topic

def test_get_quiz():
    questions = quiz.get_quiz_for_topic("llm_basics")
    assert len(questions) > 0
    assert "question" in questions[0]
    assert "options" in questions[0]
