from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_community.document_loaders import TextLoader, PyPDFLoader
model = ChatGroq(
    model="gemma2-9b-it"
)
parser = StrOutputParser()
loader = PyPDFLoader('sachin_tendulkar_biography.pdf')
docs = loader.load()
print(len(docs))
print(docs)