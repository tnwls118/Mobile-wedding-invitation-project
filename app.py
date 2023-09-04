import datetime
from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# Use MONGO_URI instead of MONGO_URL
app.config['MONGO_URI'] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)


@app.route('/write', methods=["post"])
def write():
    name = request.form.get('name')
    content = request.form.get('content')

    mongo.db['wedding'].insert_one({
        "name": name,
        "content": content
    })

    return redirect('/')


@app.route('/')
def index():
    now = datetime.datetime.now()
    wedding = datetime.datetime(2023, 8, 26, 13, 0, 0)
    diff = (wedding - now).days

    guestbooks = mongo.db['wedding'].find()

    return render_template('index.html', diff=diff, guestbooks=guestbooks)


app.run()
