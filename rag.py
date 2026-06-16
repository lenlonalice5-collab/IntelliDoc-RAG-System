from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

db = None
llm = None

def init_engine():
    global db, llm

    db = build_multi_pdf_db()

    llm = ChatOllama(model="qwen3:8b")


def get_engine():
    global db, llm

    if db is None or llm is None:
        init_engine()

    return db, llm

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5"
)

llm = ChatOllama(
    model="qwen3:8b"
)

def build_db(pdf_path):

    loader = PyPDFLoader(
        pdf_path
    )

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        docs
    )

    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory="./vector_db"
    )

    return db

def ask_question(
    db,
    question
):

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [
            d.page_content
            for d in docs
        ]
    )

    prompt = f"""
根据资料回答问题。

资料：

{context}

问题：

{question}
"""

    result = llm.invoke(
        prompt
    )

    references = []

    for d in docs:

        source = d.metadata.get(
            "source",
            "未知文件"
        )

        page = d.metadata.get(
            "page",
            0
        )

        references.append(
            f"{source} 第{page+1}页"
        )

    references = list(
        set(references)
    )

    return (
        result.content,
        references
    )

def build_multi_pdf_db():

    all_docs = []

    for file in os.listdir(
        "uploads"
    ):

        if file.endswith(
            ".pdf"
        ):

            loader = PyPDFLoader(
                os.path.join(
                    "uploads",
                    file
                )
            )

            docs = loader.load()

            all_docs.extend(
                docs
            )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(
            all_docs
        )

        db = Chroma.from_documents(
            chunks,
            embedding,
            persist_directory="./vector_db"
        )

        return db

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
