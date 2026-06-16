
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=2000&pause=500&color=7B68EE&center=true&vCenter=true&width=600&lines=📚+RAG+Platform+2.0;Enterprise+Knowledge+Base+System;Local+LLM+%2B+Vector+Retrieval" alt="Typing SVG" />
</p>

<p align="center">
  <b>⚡ 企业级本地知识库问答系统 | 完全离线 · 安全可控 · 开箱即用</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/Gradio-5.0-FF6B6B?style=for-the-badge&logo=gradio&logoColor=white">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-FF6B00?style=for-the-badge&logo=ollama&logoColor=white">
  <img src="https://img.shields.io/badge/Chroma-VectorDB-6A0DAD?style=for-the-badge&logo=chromadb&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</p>

---

## 📊 项目看板

<p align="center">
  <table>
    <tr>
      <td align="center"><b>📄 文档格式</b></td>
      <td align="center"><b>🔍 检索方式</b></td>
      <td align="center"><b>🧠 推理模型</b></td>
      <td align="center"><b>⚡ 接口</b></td>
    </tr>
    <tr>
      <td align="center">PDF</td>
      <td align="center">语义检索 (RAG)</td>
      <td align="center">Qwen / Llama</td>
      <td align="center">REST API + UI</td>
    </tr>
  </table>
</p>

---

## 📖 项目简介

RAG Platform 2.0 是一个**完全本地化部署**的企业级知识库问答系统。

> 核心理念：**让大模型读懂你的私有文档，而不泄露任何数据到公网。**

它通过 **RAG（检索增强生成）** 技术，将用户上传的 PDF 文档向量化存储，当用户提问时，系统先从知识库中检索最相关的文档片段，再交由本地大模型（Ollama）生成答案，并精确标注引用来源页码。

### 🎯 适用场景
- 企业内部文档智能问答（制度、手册、合同）
- 个人知识库管理（论文、笔记、电子书）
- 教育领域（教材问答、课程资料检索）
- 法律/医疗/金融等**数据敏感行业**

---

## ✨ 核心功能

| 功能模块 | 说明 |
| :--- | :--- |
| 📄 **多 PDF 知识库** | 支持批量上传，自动解析、切分、向量化 |
| 🔍 **RAG 语义检索** | Chroma 向量数据库，Top-K 精准召回 |
| 🧠 **本地大模型推理** | 基于 Ollama，支持 Qwen / Llama 系列，**完全离线** |
| 📌 **来源引用** | 每一条回答都附带文件名 + 页码，可溯源 |
| 💬 **对话历史** | 自动记录问答历史，支持上下文连续对话 |
| ⚡ **双端服务** | Gradio 交互界面 + FastAPI 标准 REST 接口 |
| 🐳 **容器化部署** | Docker 一键启动，环境一致性有保障 |

---

## 🏗️ 系统架构

```mermaid
flowchart TD
    A[👤 User] --> B[🌐 Gradio UI / FastAPI]
    B --> C[🧠 RAG Engine]
    C --> D[📚 Vector DB (Chroma)]
    C --> E[🧬 Embedding Model (bge-small-zh)]
    C --> F[🤖 Ollama LLM (Qwen3/Llama)]
    D --> G[📄 PDF Documents]
    F --> B
```

> 数据流：用户提问 → 向量检索 → 上下文增强 → LLM 生成 → 返回答案 + 引用

---

## 📂 项目结构

```text
RAG-Platform/
├── app.py                 # Gradio 前端界面
├── api.py                 # FastAPI 后端服务
├── rag.py                 # RAG 核心逻辑（检索 + 生成）
├── chat_history.py        # 聊天历史管理
├── requirements.txt       # Python 依赖清单
│
├── docs/                  # 📁 上传的 PDF 知识库
├── uploads/               # 📁 临时上传文件
├── vector_db/             # 📁 Chroma 向量数据库持久化
├── history/               # 📁 对话历史 JSON 存储
│
└── Dockerfile             # 🐳 Docker 镜像构建文件
```

---

## 🚀 快速开始

### 方式一：本地运行（推荐开发测试）

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/RAG-Platform.git
cd RAG-Platform

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动 Gradio 界面
python app.py
```

访问 `http://127.0.0.1:7860` 即可开始使用。

### 方式二：Docker 部署（推荐生产环境）

```bash
# 构建镜像
docker build -t rag-platform .

# 运行容器
docker run -p 8000:8000 rag-platform
```

### 方式三：FastAPI 服务化

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

API 文档地址：`http://127.0.0.1:8000/docs`

---

## 📌 API 调用示例

```http
POST /chat
Content-Type: application/json

{
  "question": "什么是决策树？",
  "history": []
}
```

**返回示例：**

```json
{
  "answer": "决策树是一种基于树结构的机器学习算法，通过特征分裂实现分类或回归...",
  "references": [
    {
      "file": "machine_learning.pdf",
      "page": 12
    },
    {
      "file": "data_mining.pdf",
      "page": 45
    }
  ]
}
```

---

## 🧠 技术栈一览

| 层级 | 技术选型 | 说明 |
| :--- | :--- | :--- |
| **前端 UI** | Gradio | 快速构建 AI 交互界面 |
| **后端 API** | FastAPI | 高性能异步 Web 框架 |
| **向量数据库** | Chroma | 轻量级嵌入式向量数据库 |
| **Embedding** | bge-small-zh | 中文语义向量模型 |
| **LLM** | Ollama (Qwen3/Llama) | 本地大模型推理引擎 |
| **文档解析** | PyPDF / LangChain | PDF 文本提取与切分 |
| **部署** | Docker + Uvicorn | 容器化 + ASGI 服务器 |

---

## 📈 版本迭代

| 版本 | 新增功能 |
| :--- | :--- |
| **v1.0** | 单 PDF 问答 + 本地 LLM |
| **v2.0** | 多 PDF 知识库 + RAG + 引用页码 + 对话历史 + FastAPI + Docker |

---

## 🚧 后续规划

- [ ] Redis 缓存加速
- [ ] 多用户系统 + 权限管理
- [ ] Vue 3 前端独立版
- [ ] RAG Agent（自动路由 + 多轮工具调用）
- [ ] 支持 Word / Excel / Markdown 格式

---

## 🧑‍💻 作者

**Lenlon**  
- AI Engineer · RAG Enthusiast · LLM Builder
- GitHub: [@lenlon](https://github.com/lenlonalice5-collab)

---

## 📜 许可证

MIT License © 2025 Lenlon

---

<p align="center">
  <b>⭐ 如果这个项目对你有帮助，欢迎 Star 支持！</b>
</p>

<p align="center">
  <img src="https://api.star-history.com/svg?repos=your-username/RAG-Platform&type=Date" width="400" />
</p>
```
