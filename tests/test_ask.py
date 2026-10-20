import sys
from types import SimpleNamespace

from app import ask as ask_module


def test_ask_keeps_follow_up_questions_in_one_chat(monkeypatch, capsys):
    class FakeChat:
        def __init__(self):
            self.questions = []

        def send_message(self, question):
            self.questions.append(question)
            return SimpleNamespace(text=f"回答: {question}", usage_metadata=None)

    chat = FakeChat()
    client = SimpleNamespace(chats=SimpleNamespace(create=lambda model: chat))
    monkeypatch.setattr(ask_module.genai, "Client", lambda api_key: client)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")
    monkeypatch.setattr(sys, "argv", ["app.ask", "最初の質問"])
    answers = iter(["続きの質問", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    ask_module.main()

    assert chat.questions == ["最初の質問", "続きの質問"]
    assert "回答: 最初の質問" in capsys.readouterr().out