from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_community.document_loaders import TextLoader
model = ChatGroq(
    model="gemma2-9b-it"
)
parser = StrOutputParser()
prompt = PromptTemplate(
    template="Write the summary of following text : {text}",
    input_variables=['text']
)
chain = prompt | model | parser
loader = TextLoader('cricket_info.txt')
docs = loader.load()
print(len(docs))
print(docs)
print(docs[0].page_content)
print(docs[0].metadata)
#print(chain.invoke({'text':docs[0].page_content}))