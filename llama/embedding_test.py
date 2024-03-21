"""
Document loading for local embeddings and vector storage. 
Reference: https://python.langchain.com/docs/use_cases/question_answering/local_retrieval_qa#document-loading 

TODO: it's not working so make it working if switching to local index db
"""

#%%
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

print(all_splits)

#%%

import os
import json
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma

print(os.environ)

vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())
# %%

question = "What are the approaches to Task Decomposition?"
docs = vectorstore.similarity_search(question)
len(docs)

# %%
