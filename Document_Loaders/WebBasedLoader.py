from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_community.document_loaders import WebBaseLoader
model = ChatGroq(
    model="gemma2-9b-it"
)
url = 'https://www.amazon.in/Running-Jordan-6-White-Metallic-Gold-Black-Fq8298-101-8Uk/dp/B0D91V35Q8/ref=sr_1_1?nsdOptOutParam=true&sr=8-1&psc=1'
loader = WebBaseLoader(url)
docs = loader.load()
prompt = PromptTemplate(
    template = "Answer the following question \n {question} from the following text - \n {text}",
    input_variables=['question','text']
)
chain = prompt | model | StrOutputParser()

print(chain.invoke({'question':'What product we are talking about ?','text':docs[0].page_content}))