from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_community.document_loaders import CSVLoader
model = ChatGroq(
    model="gemma2-9b-it"
)
loader = CSVLoader(file_path='student.csv')
docs = loader.load()
print(len(docs))
print(docs[0].page_content)