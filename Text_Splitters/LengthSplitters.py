from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader('sachin_tendulkar_biography.pdf')
docs = loader.load()
splitter = CharacterTextSplitter()
splits = splitter.split_documents(docs)
print(splits)