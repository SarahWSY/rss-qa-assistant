import os
import json
import feedparser
from langchain_community.document_loaders import JSONLoader


def read_feed_to_json(rss_url, json_file_path):

    # Get and parse the rss feed into a dictionary
    parser = feedparser.parse(rss_url)

    # Extract the entries list from the dictionary
    entries = parser.get('entries')

    # Create an empty list to store just the important information
    entries_short = []

    for entry in entries:
        entries_short.append({'title': entry['title'],
                            'summary': entry['summary'],
                            'link': entry['link'],
                            'published': entry['published']})

    with open(json_file_path, "w") as file:
        json.dump(entries_short, file)


def load_json_news(file_path):
    # Loading the news as langchain documents
    loader = JSONLoader(
        file_path=file_path,
        jq_schema='.[]',
        text_content=False)
    news = loader.load()

    return news

