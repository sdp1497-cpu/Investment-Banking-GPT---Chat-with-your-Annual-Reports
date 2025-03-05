
#References 

# The below code is refrenced from https://github.com/nicknochnack/Llama2RAG/blob/main/app.py  with modifications done by Sonia Patel.
# https://streamlit.io/components?category=page-navigation
# https://docs.llamaindex.ai/en/stable/getting_started/installation.html
# https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
# https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# https://docs.llamaindex.ai/en/stable/examples/embeddings/Langchain.html


import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
import torch
from llama_index.core import PromptTemplate
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.langchain import LangchainEmbedding
from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index.core.indices.service_context import ServiceContext
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, download_loader
from pathlib import Path
from llama_index.core import download_loader
from llama_index.core import Document
import time 
#Resued code from https://github.com/nicknochnack/Llama2RAG 
name = "meta-llama/Llama-2-7b-chat-hf"  # Define variable to hold llama2 weights naming
auth_token = "******" #my auth token

@st.cache_resource
def get_tokenizer_model():
    tokenizer = AutoTokenizer.from_pretrained(name, token=auth_token, cache_dir='./model/')

    # Code by Sonia Patel 
    model = AutoModelForCausalLM.from_pretrained(
        name,
        cache_dir='./model/',
        token=auth_token,
        torch_dtype=torch.float32
    )

    return tokenizer, model
tokenizer, model = get_tokenizer_model()

# Code by Sonia Patel 
system_prompt = """<s>[INST] <<SYS>>  
You are a helpful, respectful and honest assistant. Always answer as   
helpfully as possible, while being safe. Your answers should not include
any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.
Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain 
why instead of answering something not correct. If you don't know the answer 
to a question, please don't share false information or random information.

Your goal is to provide answers relating to the financial performance of 
the companies in the uploaded annual reports for comparative analysis and insights.<</SYS>>
"""
#Resued code from https://github.com/nicknochnack/Llama2RAG 
query_wrapper_prompt = PromptTemplate("<|USER|>{query_str} [/INST]") # Throw together the query wrapper
llm = HuggingFaceLLM(context_window=4096,
                    max_new_tokens=256,
                    system_prompt=system_prompt,
                    query_wrapper_prompt=query_wrapper_prompt,  # Create a HF LLM using the llama index wrapper
                    model=model,
                    tokenizer=tokenizer)



embeddings = LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # Create and download embeddings instance
)

# Code by Sonia Patel 
Settings.llm = llm    
Settings.embed_model = embeddings # My code  
Settings.chunk_size = 1024 # My code 

#Resued code from https://github.com/nicknochnack/Llama2RAG 
# Download PDF Loader
PyMuPDFReader = download_loader("PyMuPDFReader")
# Create PDF Loader
loader = PyMuPDFReader()


# Code by Sonia Patel 
st.sidebar.header("🏦Welcome to IB GPT🏦")  
# Create a file uploader in Streamlit that accepts only PDF files
uploaded_files = st.sidebar.file_uploader("📁 Upload 1 or more PDF files", type="pdf", accept_multiple_files=True)  
if uploaded_files:
      
    documents = [loader.load(file_path=Path(file.name), metadata=True) for file in uploaded_files] 
    indices = [VectorStoreIndex.from_documents(doc) for doc in documents] 
    query_engines = [index.as_query_engine() for index in indices] 
    st.title('Investment Banking GPT ') 
# Create centered main title 
    st.title('🦙 Using Llama2-RAG') 
    # Create a text input box for the user
    prompt = st.text_input('Hello 👋 Input your prompt here') 
# If the user hits enter
    if prompt:
       
        # Code by Sonia Patel 
        responses = [qe.query(prompt) for qe in query_engines]  
        for response in responses:  
            st.write(response)
            with st.subheader('Response Object'):
                st.write(response)
            with st.subheader('Source Text'):
                st.write(response.get_formatted_sources())
