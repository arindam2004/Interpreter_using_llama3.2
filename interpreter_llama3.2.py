"""
Explain-Code • Uses Llama 3.2 via Ollama
This is comparatively slower to generate
output than paid models.
"""

# ── Imports ──────────────────────────────────────────────────────────────
import os
from IPython.display import Markdown, display           # Jupyter only
import ollama

# ── Constants ───────────────────────────────────────────────────────────
MODEL_LLAMA = "llama3.2"        # replace with the exact tag shown by `ollama list`

SYSTEM_PROMPT = (
    "You are a technical assistant who explains code step-by-step, analyses "
    "time/space complexity, and suggests optimisations."
)

QUESTION = """
Please explain what this code does and why:

sorted([
    x**2
    for x in (
        lambda f, l: sum(
            [f(f, i) if isinstance(i, list) else [i] for i in l],
            []
        )
    )(
        lambda f, l: sum(
            [f(f, i) if isinstance(i, list) else [i] for i in l],
            []
        ),
        [[1, 2, [3, 'a']], [4, [5, [6, None]]]]
    )
    if isinstance(x, int)
])
"""

USER_PROMPT = "Please elaborate and explain the code:\n" + QUESTION.strip()

MESSAGES = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user",   "content": USER_PROMPT},
]

# ── Call Ollama with error handling ─────────────────────────────────────
try:
    response = ollama.chat(model=MODEL_LLAMA, messages=MESSAGES)
    reply = response["message"]["content"]
    display(Markdown(reply))              # Works only inside Jupyter
except ollama.OllamaError as err:
    print(f"[Ollama error] {err}")
except Exception as exc:
    print(f"[Unexpected error] {exc.__class__.__name__}: {exc}")