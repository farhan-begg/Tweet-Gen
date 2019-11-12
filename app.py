from flask import Flask, render_template, request, redirect, url_for
from sample import main_sample
from histogram import histogram_dict
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# import os

app = Flask(__name__)

# host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweet-generator-sh')
# client = MongoClient(host=f'{host}?retryWrites=false')
# db = client.get_default_database()
# tweet = db['tweet']

@app.route('/')
def index():
    """Return Homepage"""
    sentence_size = 10
    sentence_list = []
    text = 'test.txt'
# Andrey's help
    for i in range(0, sentence_size):
        sentence_list.append(main_sample(text))
    sentence_string = " ".join(sentence_list)
    
    return render_template('index.html', sentence=sentence_string)

if __name__ == '__main__':
    app.run(debug=True)
