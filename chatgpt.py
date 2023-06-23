import os
import sys

import constants


import openai
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import Docx2txtLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma, DocArrayInMemorySearch


os.environ["OPENAI_API_KEY"] = constants.APIKEY


file = "Filmography.docx"
loader = Docx2txtLoader(file)
# loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders(
    [loader]
)

query = "Please can you get 5 movies, and summarize each one into 5 words. Then try to guess the genre"

response = index.query(query)


print(response)
