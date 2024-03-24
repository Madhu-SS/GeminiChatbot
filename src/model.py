from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from src.data import DataLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import sys


load_dotenv()
google_api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

llm = ChatGoogleGenerativeAI(model="gemini-pro")

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

data=DataLoader()

text_splitter=CharacterTextSplitter(separator='\n',
                                    chunk_size=500,
                                    chunk_overlap=50)

text_chunks=text_splitter.split_documents(data)

db = FAISS.from_documents(text_chunks, embeddings)
db.save_local("vectorstore")

custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])

qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=db.as_retriever(search_kwargs={'k': 2}),
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt': prompt}
                                       )

def chat(query):
    result=qa_chain.invoke(query)
    response=result['result']
    return response
# query='tell me about Potentiam'
# result=qa_chain.invoke(query)
# print(result)






