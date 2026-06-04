# rag_local_ai
本地知识库问答系统（RAG）项目，使用LangChain+Chroma+Ollama
# 本地知识库问答系统 (RAG)

> 一个基于 LangChain、Chroma、Ollama 的本地知识库问答系统，实现 PDF 文档上传、向量化检索和大模型智能回答。

---

## 功能特点

- ✅ 本地运行，无需网络连接或 API Key  
- ✅ 支持上传 PDF 文档，并自动解析文本  
- ✅ 基于 Chroma 向量数据库进行相似度检索  
- ✅ 使用 Ollama Qwen3 模型进行生成式问答  
- ✅ Gradio Web 界面，简洁直观  
- ✅ 支持多轮问答和上下文记忆  

---

## 技术栈

- **Python**  
- **LangChain** (RAG + 文档加载 + Prompt 管理)  
- **Chroma** (向量数据库)  
- **Ollama** (本地大语言模型)  
- **Gradio** (Web界面)  
- **PDF2Image / RapidOCR** (扫描PDF OCR识别，可选)  

---

## 安装指南

1. 克隆仓库：

```bash
git clone https://github.com/你的用户名/你的仓库名.git
cd 你的仓库名
```


## 创建虚拟环境并激活：
```bash
python -m venv venv
# Windows CMD
venv\Scripts\activate.bat
# 或 PowerShell
venv\Scripts\Activate.ps1
安装依赖：
pip install -r requirements.txt
# 或手动安装：
pip install langchain langchain-ollama chromadb gradio pdf2image pillow rapidocr-onnxruntime
```
## 下载 Ollama Qwen3 模型：
```
ollama run qwen3:8b
```
## 使用说明
将 PDF 文档放入 docs/ 文件夹<br>
运行应用：
python app.py<br>
打开浏览器访问：
http://127.0.0.1:7860<br>
在页面中输入问题，系统会基于上传的文档生成答案。
项目结构<br>
rag_project/<br>
│<br>
├─ app.py            # 主程序入口<br>
├─ docs/             # PDF 文档存放目录<br>
├─ vector_db/        # Chroma向量数据库（第一次运行后生成）<br>
├─ venv/             # Python虚拟环境<br>
├─ README.md<br>
└─ requirements.txt<br>
示例效果<br>

问题： 什么是决策树？<br>

回答： 根据文档第12页：决策树是一种监督学习算法，用于分类和回归……<br>

升级计划:<br>
 支持多个 PDF 同时上传<br>
 输出答案引用页码<br>
 增加聊天历史记录功能<br>
 Docker 容器化部署<br>
 FastAPI 接口扩展<br>
 
许可证<br>
MIT License<br>

联系方式<br>
邮箱：lenlonalice@gmail.com<br>
GitHub：https://github.com/lenlonalice5-collab
