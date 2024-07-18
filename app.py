from flask import Flask, request, jsonify
from app_helper import *
from app_qa_helper import *
from app_podcast_helper import *


app = Flask(__name__)

JSON_FILE_PATH='./news.json'
CHROMA_PERSIST_DIR = 'chroma/'
RSS_URL = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"


@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    question = data.get("question")
    answer = llm_answer(question, vectordb)
    return jsonify({"answer": answer}), 200


@app.route("/podcast", methods=["GET"])
def podcast():
    script = generate_script(news)
    return jsonify({"script": script}), 200


if __name__ == "__main__":
    read_feed_to_json(RSS_URL, JSON_FILE_PATH)
    wipe_chroma_directory(CHROMA_PERSIST_DIR)
    news = load_json_news(JSON_FILE_PATH)
    vectordb = create_vectordb(news, CHROMA_PERSIST_DIR)
    app.run(debug=True)
    