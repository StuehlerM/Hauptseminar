from flask import Flask
import codecs
#import tensorflow as tf

app = Flask(__name__)

@app.route('/')
def index():
    indexPage = open('HTML\index.html', 'r', encoding='utf-8')
    return indexPage.read()

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0')