from rag import *
from chat_history import *
import gradio as gr

db = build_multi_pdf_db()

def chat(question):

    answer,references = ask_question(
        db,
        question
    )

    save_history(
        question,
        answer
    )

    return f"""
{answer}

================

参考来源：

{chr(10).join(references)}
"""



ui = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text"
)

ui.launch()