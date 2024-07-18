# RSS News assistant
#### Description:
This is an API tool which reads an RSS news feed and answers related questions. It is also able to generate a podcast script from the RSS news feed.
The API was developed using Flask. 
The question-answering (RAG) and podcast generation (summarization/transformation) functions were developed using LangChain. Llama3 model is used for both question-answering and podcast generation functions. It uses Ollama to run the Llama3 model locally. 

#### Demo:
Question-answering is done with a POST request to /query with the JSON request body like below:
![image](https://github.com/user-attachments/assets/c9e8fa74-dba0-4d9e-aecf-7ed6296da608)
![image](https://github.com/user-attachments/assets/f11e95fd-e082-412d-adf0-ecb42a9641e8)

Podcast generation is done with a GET request to /podcast:
![Screenshot from 2024-07-18 20-07-46](https://github.com/user-attachments/assets/eeab1207-3af2-4576-bd1c-59401a64f41f)

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
