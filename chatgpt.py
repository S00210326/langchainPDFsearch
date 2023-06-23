import os
import sys


import openai
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import Docx2txtLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma, DocArrayInMemorySearch
from dotenv import load_dotenv

load_dotenv()

# now you can access your environment variables like this:


openai_api_key = os.getenv("OPENAI_API_KEY")


file = "Filmography.docx"
loader = Docx2txtLoader(file)
# loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders(
    [loader]
)

query = "Please can you get 5 movies, and summarize each one into 5 words. Then try to guess the genre"

response = index.query(query)


print(response)
