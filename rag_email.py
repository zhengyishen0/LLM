from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
import pandas as pd
import os


# Load the email pairs from the CSV file
file_path = "data/emails.csv"
csv_path = "data/email_pairs.csv"
index_path = "data/email_index.index"


# Load email pairs from the CSV file
def load_csv_data(file_path, csv_path):
    data = pd.read_csv(file_path)
    filtered_data = data[['subject_original', 'body_original', 'body_reply']]
    filtered_data.to_csv(csv_path, index=False)


# Load email data from the CSV or Index file
def load_index(csv_path, index_path):
    if os.path.isfile(index_path):
        vector = FAISS.load_local(index_path)
        return vector

    loader = CSVLoader(csv_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vector = FAISS.from_documents(documents, embeddings)

    vector.save_local(index_path)
    return vector


vector = load_index(csv_path, index_path)
retriever = vector.as_retriever()

template = """
Please write an proper email on behalf Zhengyi Shen to reply the income email based only on the provided context:

<context>
{context}
</context>

Email: {input}
"""


# Construct the chain
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
output_parser = StrOutputParser()
retrieval = RunnableParallel(context=retriever, input=RunnablePassthrough())
# retrieval = {"context": retriever, "input": RunnablePassthrough()}

chain = retrieval | prompt | model | output_parser


# Invoke the chain
mail = """
hi Zhengyi,

It's good to talking with you last time. Sorry I forgot your school name. Could you please tell me again? 

Best,
Kim

"""

response = chain.invoke(mail)
print(response)
