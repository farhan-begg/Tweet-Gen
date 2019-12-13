from flask import Flask, render_template, request, redirect, url_for
from markov2 import word_generator
import dictogram


# from sample import main_sample
# from histogram import histogram_dict

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    sentence = word_generator()

    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)
