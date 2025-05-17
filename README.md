# Explain‑Code with Llama 3 via Ollama

A lightweight Python script that sends a code snippet to **Llama 3** (served locally by [Ollama](https://ollama.ai)) and returns a step‑by‑step explanation plus optimization hints.

> **Heads‑up:** Local inference is slower than hosted paid models, but you keep everything on‑device.

---

## ✨ Features

- Works with any Ollama model tag (default: `llama3.2`)
- System prompt asks for explanation **and** complexity / optimization analysis
- Rich Markdown output in Jupyter, graceful fallback to `print`
- Basic error handling (`ollama.OllamaError` or generic exceptions)

---

## 🖥 Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.8 + | Run the script |
| Ollama | ≥ 0.6 | Serve the LLM locally |
| IPython / Jupyter | optional | Pretty Markdown rendering |

Install Ollama on macOS:

```bash
brew install ollama
ollama serve &        # start the local server
ollama pull llama3    # download a model
```

---

## 🚀 Usage

```bash
python interpreter_llama3.2.py
```

The default `QUESTION` variable contains a gnarly nested list‑comprehension.  
Edit it (or wrap the logic in a function) to analyze any snippet you like.

---

## 🔧 Configuration

| Variable | Description |
|----------|-------------|
| `MODEL_LLAMA` | Ollama model tag (e.g. `llama3.2`, `llama3:8b-q4_K_M`) |
| `SYSTEM_PROMPT` | System role prompt |
| `QUESTION` | Code to explain |

---

## 🗂 Files

```
interpreter_llama3.2.py   # main script
Sample_output.doc         # sample output of the question
README.md
```

---

## 📜 Mini‑script (core logic)

```python
import ollama
from IPython.display import Markdown, display

MODEL_LLAMA = "llama3"
SYSTEM_PROMPT = "You are a technical assistant..."
QUESTION = "sorted([x**2 for x in ...])"

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user",   "content": "Please elaborate:\n" + QUESTION}
]

try:
    reply = ollama.chat(model=MODEL_LLAMA, messages=messages)["message"]["content"]
    display(Markdown(reply))
except ollama.OllamaError as e:
    print(f"Ollama error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 🤝 Contributing

PRs welcome! Ideas:

- Stream replies for real‑time progress
- CLI arguments instead of hard‑coded strings
- Unit tests

---

## 📄 License

MIT
