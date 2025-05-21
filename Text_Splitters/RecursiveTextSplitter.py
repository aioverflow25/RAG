from langchain.text_splitter import RecursiveCharacterTextSplitter
text = '''
Natural Language Processing (NLP) is a branch of artificial intelligence that enables machines to understand, interpret, and generate human language. It combines computational linguistics with machine learning to process text and speech data in a meaningful way.

 NLP powers a wide range of applications, including language translation, sentiment analysis, chatbots, and voice assistants. By analyzing syntax, semantics, and context, NLP helps computers comprehend not just what is said, but what is meant. As the volume of human language data grows, NLP plays an essential role in making that information accessible, useful, and interactive across industries and technologies
'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10
)
docs = splitter.split_text(text)
print(len(docs))
print(docs)