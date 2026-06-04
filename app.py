from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    "docs/machine_learning.pdf"
)

docs = loader.load()

print(len(docs))
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print(len(chunks))
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5"
)

db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="./vector_db"
)
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:8b"
)
query = "什么是决策树"

docs = db.similarity_search(
    query,
    k=3
)

for d in docs:
    print(d.page_content)
context = "\n".join(
    [d.page_content for d in docs]
)

prompt = f"""
根据以下内容回答：

{context}

问题：
什么是决策树
"""

response = llm.invoke(prompt)

print(response.content)
import gradio as gr

def chat(question):
    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [d.page_content for d in docs]
    )

    prompt = f"""
    根据资料回答：

    {context}

    问题：
    {question}
    """

    result = llm.invoke(prompt)

    return result.content

ui = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text"
)

ui.launch()