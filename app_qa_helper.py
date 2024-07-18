import os
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings


def wipe_chroma_directory(chroma_dir):
    if os.path.exists(chroma_dir):
        for file_name in os.listdir(os.path.join(os.getcwd(), chroma_dir)):
            file_path = os.path.join(os.getcwd(), chroma_dir, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)


def create_vectordb(news, chroma_dir):
    ollama_emb = OllamaEmbeddings(
    model="llama3",
    model_kwargs={'device': 'cuda'}
    )
    
    vectordb = Chroma.from_documents(
        documents=news,
        embedding=ollama_emb,
        persist_directory=chroma_dir
    )

    return vectordb


def create_qa_prompt():
    # Define prompt
    qa_prompt_template = """You are a news assistant which answers questions about world news.
                            Your answers should be based only on the news context provided below.
                            Do not reply with the context documents, instead give a direct answer by rephrasing relevant pieces of contexts.
                            If the question cannot be answered with the information provided in the news context, just state so.
                            Keep your answer short and concise.

                            Context: {context}

                            ---

                            Question: {question}

                            ---
                            Helpful Answer:
                            """

    # Instantiation using from_template
    qa_prompt = PromptTemplate.from_template(qa_prompt_template)

    return qa_prompt


def create_qa_chain(vectordb, query_prompt, model="llama3"):
    # Define llm model 
    llm = Ollama(model=model, temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 10}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": query_prompt})

    return qa_chain


def llm_answer(question, vectordb):

    qa_prompt = create_qa_prompt()

    qa_chain = create_qa_chain(vectordb, qa_prompt)

    answer = qa_chain.invoke({"query": question})["result"]

    return answer
