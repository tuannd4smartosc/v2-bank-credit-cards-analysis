# app/agents/writer.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import os

llm = ChatOpenAI(model="gpt-4", temperature=0.7)

def generate_section():
    prompt = PromptTemplate.from_template("Write a 300-word section on {topic}.")
    chain = prompt | llm
    response = chain.invoke({"topic": "emerging AI trends"})
    return {"content": response.content}
