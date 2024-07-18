from langchain.chains.llm import LLMChain
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain


def create_podcast_prompt():
    # Define prompt
    podcast_prompt_template = """Write a podcast script of about 600 to 800 words based on the news items provided below, delimited by triple backticks.

    news: ```{text}```

    The output should start with a title line, followed by the podcast script content.

    Script:"""

    prompt = PromptTemplate.from_template(podcast_prompt_template)

    return prompt


def create_stuff_chain(prompt):
    # Define llm model (Llama3 context window is ~8000 tokens, sufficient to use stuff prompting)
    llm = Ollama(model="llama3", temperature=0)

    # Define LLM chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    return stuff_chain


def generate_script(news):

    prompt = create_podcast_prompt()

    stuff_chain = create_stuff_chain(prompt)

    # Invoke the chain to get response
    script = stuff_chain.invoke(news)["output_text"]

    # Save script to file
    with open("podcast_script.txt", "w") as file:
        file.write(script)
    
    return script
