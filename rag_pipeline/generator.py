"""
Module for generating video scripts using an LLM.
"""
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI


def generate_script(docs, query="Summarize this for a video explainer"):
    llm = OpenAI(temperature=0.3)
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain.run(input_documents=docs, question=query)