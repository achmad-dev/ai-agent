import os 
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import OpenAI


dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

os.environ['OPENAI_API_KEY'] = os.getenv("OPEN_AI_API_KEY")

#App Framework
st.title(" Bussiness Idea pros and cons")
prompt = st.text_input('Write your Bussiness idea here')

#Prompt Templates
idea_template = PromptTemplate(
    input_variables = ['idea'],
    template="Write me pros and cons of my bussiness idea here and chance of profitability: {idea}"
)

# Memory
idea_memory = ConversationBufferMemory(input_key='idea', memory_key='chat_history')

# LLms
llm = OpenAI(model='gpt-3.5-turbo-instruct',
             temperature=0.7)

idea_chain = LLMChain(
    llm=llm,
    prompt=idea_template,
    output_key='idea',
    memory=idea_memory,
    verbose=True
)


# Shows response to the screen
if prompt:
    idea = idea_chain.run(prompt)

    st.write(idea)

    with st.expander('Bussiness idea History'):
        st.info(idea_memory.buffer)