from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI


def generate_script(docs, query):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain.run(input_documents=docs, question=query)