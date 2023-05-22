import streamlit as st
import os

from dotenv import load_dotenv, find_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain


# Load environment
load_dotenv(find_dotenv('../.env'))

@st.cache_resource
def initialize():
    # Initialize the model
    model = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0
    )
    
    # Initialize loader
    filepath = "Fluent Python.pdf"
    loader = PyPDFLoader(filepath)
    docs = loader.load_and_split()

    # Initialize Embeddings
    embeddings = OpenAIEmbeddings()

    # Store embeddings into vector DB
    vector_store = Chroma.from_documents(
        docs,
        embeddings,
        collection_name="fluent-python",
        persist_directory="../chroma"
    )
    return (
        ConversationalRetrievalChain.from_llm(
            llm=model,
            retriever=vector_store.as_retriever(),
            return_source_documents=True
        ),
        docs
    )
    
chain, docs = initialize()
st.title("Fluent Python GPT")
prompt = st.text_input("Plug in the prompt here:")

if prompt:
    # Generate answer
    response = chain({
        "question": prompt,
        "chat_history": ""  # Due to the refresh limitation of Streamlit, we will leave this as empty
    })
    
    # Retrieve the answer
    answer = response["answer"]
    source = response["source_documents"]
    
    # Displaying answers
    st.write("### Answer")
    st.write(answer)
    st.write("### Related pages as references")
    for document in source:
        st.write(document.metadata["page"])
        st.write(document.page_content)