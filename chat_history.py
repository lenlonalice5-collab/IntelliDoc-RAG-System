import json
import os

def save_history(
    question,
    answer
):

    os.makedirs(
        "history",
        exist_ok=True
    )

    file_path = "history/chat.json"

    if os.path.exists(
        file_path
    ):

        with open(
            file_path,
            "r",
            encoding="utf8"
        ) as f:

            data = json.load(f)

    else:

        data = []

    data.append(
        {
            "question":question,
            "answer":answer
        }
    )

    with open(
        file_path,
        "w",
        encoding="utf8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

def load_history():

    file_path = "history/chat.json"

    if not os.path.exists(
        file_path
    ):

        return []

    with open(
        file_path,
        "r",
        encoding="utf8"
    ) as f:

        return json.load(f)


def chat(question, db, llm):
    docs = db.similarity_search(question, k=3)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
根据资料回答问题。

资料：

{context}

问题：

{question}
"""

    result = llm.invoke(prompt)

    references = []

    for d in docs:
        source = d.metadata.get("source", "未知文件")
        page = d.metadata.get("page", 0)
        references.append(f"{source} 第{page+1}页")

    reference_text = "\n".join(references)

    return f"""
{result.content}

====================

参考来源：

{reference_text}
"""