from flask import Flask, render_template, request, redirect, url_for
from sample import main_sample
from histogram import histogram_dict

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    
    sentence_size = 10
    sentence_list = []
    text = 'test.txt'

    for i in range(0, sentence_size):
        sentence_list.append(main_sample(text))
    sentence_string = " ".join(sentence_list)
    
    return render_template('index.html', sentence=sentence_string)

if __name__ == '__main__':
    app.run(debug=True)
