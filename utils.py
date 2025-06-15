# utils.py
import os
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

VECTORSTORE_PATH = "vectorstore"
openai_key = os.getenv("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")

# Load vectorstore from PDF files
def load_vectorstore():
    pdf_files = [f for f in os.listdir(VECTORSTORE_PATH) if f.endswith(".pdf")]
    if not pdf_files:
        raise FileNotFoundError("No policy PDF found in vectorstore.")

    docs = []
    for pdf in pdf_files:
        loader = PyPDFLoader(os.path.join(VECTORSTORE_PATH, pdf))
        docs.extend(loader.load())

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

retriever = load_vectorstore().as_retriever()
llm = ChatOpenAI(
    temperature=0.3,
    api_key=openai_key,
    base_url="https://openrouter.ai/api/v1",
    model="mistralai/mixtral-8x7b"
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

def get_answer(query):
    result = qa_chain.invoke(query)
    answer = result['result']
    sources = result.get('source_documents', [])
    if sources:
        refs = "\n\n📌 **References:**\n"
        for i, doc in enumerate(sources[:3], start=1):
            refs += f"{i}. Page {doc.metadata.get('page', '?')} - File: {doc.metadata.get('source', '?')}\n"
        answer += refs
    return answer
