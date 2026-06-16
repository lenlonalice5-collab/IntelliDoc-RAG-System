
# 🚀 RAG Platform 2.0

<p align="center">
  <b>Enterprise-Level Local RAG Knowledge Base System</b><br>
  基于本地大模型的企业级知识库问答系统（2.0版本）
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue">
  <img src="https://img.shields.io/badge/FastAPI-API-green">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-orange">
  <img src="https://img.shields.io/badge/Chroma-VectorDB-purple">
  <img src="https://img.shields.io/badge/Docker-Deploy-blue">
</p>

---

# 📖 1. Project Overview | 项目简介

RAG Platform 2.0 是一个完整的本地知识库问答系统，基于大语言模型 + 向量数据库构建。

支持：

- 📄 多PDF文档上传与解析
- 📚 向量检索（RAG）
- 🧠 本地大模型 Ollama 推理
- 📌 精确引用页码
- 💬 对话历史记录
- ⚡ FastAPI 接口服务化
- 🐳 Docker 一键部署

---

# ✨ 2. Key Features | 核心功能

## 📄 Multi-PDF Knowledge Base
- 支持多个 PDF 同时上传
- 自动文本切分（chunking）
- 自动向量化存储

---

## 🔍 RAG Retrieval System
- 基于 Chroma 向量数据库
- 语义检索 Top-K 文档
- 提高回答准确性

---

## 🧠 Local LLM (Ollama)
- 支持 Qwen / Llama 等本地模型
- 完全离线运行
- 无需 OpenAI API

---

## 📌 Source Citation (引用页码)
- 每个答案返回：
  - 文件名
  - 页码
- 提高可解释性

---

## 💬 Chat History
- 自动记录问答历史
- 支持后续扩展用户系统

---

## ⚡ FastAPI Backend
- REST API接口化
- 支持前后端分离
- 可用于 Web / APP 调用

---

## 🐳 Docker Deployment
- 一键容器化部署
- 环境一致性保证
- 支持云端部署

---

# 🏗️ 3. System Architecture | 系统架构

```text
User
 ↓
Gradio UI / FastAPI
 ↓
RAG Engine
 ↓
Vector DB (Chroma)
 ↓
Embedding Model (bge-small-zh)
 ↓
Ollama LLM (Qwen3 / Llama)
````

---

# 📂 4. Project Structure

```text
RAG-Platform/
│
├── app.py                 # Gradio前端
├── api.py                # FastAPI服务
├── rag.py                # RAG核心逻辑
├── chat_history.py      # 聊天历史管理
├── requirements.txt
│
├── docs/                # PDF知识库
├── uploads/             # 上传文件
├── vector_db/           # 向量数据库
├── history/             # 历史记录
│
└── Dockerfile
```

---

# 🚀 5. How to Run | 运行方式

## 5.1 安装依赖

```bash
pip install -r requirements.txt
```

---

## 5.2 启动 Gradio

```bash
python app.py
```

访问：

```
http://127.0.0.1:7860
```

---

## 5.3 启动 FastAPI

```bash
uvicorn api:app --reload
```

访问API文档：

```
http://127.0.0.1:8000/docs
```

---

# 🐳 6. Docker Deployment

## 6.1 构建镜像

```bash
docker build -t rag-platform .
```

---

## 6.2 运行容器

```bash
docker run -p 8000:8000 rag-platform
```

---

# 📌 7. API Example

### 请求：

```json
POST /chat
{
  "question": "什么是决策树"
}
```

### 返回：

```json
{
  "answer": "...",
  "references": [
    "machine_learning.pdf 第12页"
  ]
}
```

---

# 🧠 8. 2.0 Upgrade Summary | 2.0升级总结

本版本（RAG Platform 2.0）实现：

* ✔ 多PDF知识库支持
* ✔ 向量检索增强（RAG）
* ✔ 引用页码（可解释AI）
* ✔ 聊天历史记录
* ✔ FastAPI服务化
* ✔ Docker容器化部署

---

# 🚀 9. Future Roadmap | 后续规划

* Redis缓存优化
* 多用户系统
* 前端Vue版本
* 权限管理
* RAG Agent增强版

---

# 🧑‍💻 Author

Built by **Lenlon**

Focus:

* AI Engineering
* RAG Systems
* LLM Applications

---

# 📜 License

MIT License
