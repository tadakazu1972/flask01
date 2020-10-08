from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

def picked_up():
    messages = [
        "コココ、あなたの名前を入力してよねぇ。ンフ。",
        "おお！そなたの名は何と申されるのか？",
        "名は何という？"
    ]
    return np.random.choice(messages)

@app.route('/')
def index():
    title = "Welcome"
    message = picked_up()
    return render_template('index.html', message=message, title=title)

@app.route('/post', methods=['GET','POST'])
def post():
    title = "Hello"
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html', name=name, title=title)
    else:
        #エラーなどでリダイレクトしたい場合
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0') #どこからでもアクセス可能
