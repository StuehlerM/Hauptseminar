from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import os
import tensorflow as tf
from PIL import Image

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imageReceive',  methods=['GET', 'POST'])
def imageReceive():
    if request.method == 'POST':
        print(request.form)
        print()
        for file in request.files.getlist("imageInput"):
            print(file.filename)
        #img = Image.open()
        return 'Success!'

    if request.method == 'GET':    
        return render_template('index.html')       

@app.route('/imageSend')
def imageSend():
    if request.args.get('type') == '1':
       filename = 'ok.gif'
    else:
       filename = 'error.gif'
    return send_file(filename, mimetype='image/gif')

@app.route('/text',  methods=['POST'])
def textTest():
    if request.method == 'POST':
        result = request.form
        print(result)
        return "ok"


if __name__ == '__main__':
    print(os.getcwd())
    app.run(debug=True)

    #app.run(host='0.0.0.0')