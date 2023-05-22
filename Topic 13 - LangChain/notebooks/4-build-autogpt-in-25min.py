# Following the video: https://www.youtube.com/watch?v=MlK6SIjcjE8
import streamlit as st

from dotenv import load_dotenv, find_dotenv

from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

# Load environment
load_dotenv(find_dotenv('../.env'))

# App framework
st.title("AutoGPT application - Explain any concept for kids")
temperature = st.selectbox(
    label="Model temperature",
    options=[0, 0.1, 0.2, 0.4, 0.6, 0.8, 1]
)
prompt = st.text_input("Plug in the concept here:")

# LLM initialization
llm = OpenAI(temperature=temperature)

# Memory
memory = ConversationBufferMemory(
    input_key='concept',
    memory_key='chat_history'
)

# Wikipedia API Wrapper
wiki = WikipediaAPIWrapper()

# Show answer returned from the LLM if there is a prompt
if prompt:
    seven_yo_concept_template = PromptTemplate(
        input_variables=['concept'],
        template="Explain {concept} to a 7-year-old kid."
    )
    high_school_concept_template = PromptTemplate(
        input_variables=['concept'],
        template="Explain {concept} to a high school student."
    )
    wiki_output = wiki.run(prompt)
    
    seven_yo_concept_chain = LLMChain(llm=llm, prompt=seven_yo_concept_template, verbose=True, output_key='7yo', memory=memory)
    high_school_concept_chain = LLMChain(llm=llm, prompt=high_school_concept_template, verbose=True, output_key='hs', memory=memory)
    
    sequential_chain = SequentialChain(
        chains=[seven_yo_concept_chain, high_school_concept_chain],
        verbose=True,
        input_variables=['concept'],
        output_variables=['7yo', 'hs']
    )
    
    response = sequential_chain({
        'concept': prompt
    })
    st.write("### For a 7-year-old kid")
    st.write(response['7yo'])
    st.write("### For a high school student")
    st.write(response['hs'])
    st.write("### Wikipedia search")
    st.write(wiki_output)
    
    with st.expander("Message History"):
        st.info(memory.buffer)