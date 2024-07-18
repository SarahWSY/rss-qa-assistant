# RSS News assistant
#### Description:
This is an API tool which reads an RSS news feed and answers related questions. It is also able to generate a podcast script from the RSS news feed.
The API was developed using Flask. 
The question-answering and podcast generation functions were developed using LangChain. Llama3 model is used for both question-answering and podcast generation functions. It uses Ollama to run the Llama3 model locally. 
#### Demo:

#### Installation:
Create a new conda environment with python 3.10 and install the following packages before running the application.

```bash
pip install flask
```
```bash
pip install langchain
```
```bash
pip install langchain-community
```
```bash
pip install feedparser
```
```bash
pip install jq
```
```bash
pip install chromadb
```
```bash
pip install ollama
```
Lastly, download the model to be used:
```bash
ollama pull llama3
```
