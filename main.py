from flask import Flask
from flask import jsonify
from flask import request, render_template
import pandas as pd
import wikipedia
import time
import datetime


app = Flask(__name__)

@app.route('/')
def root():
    return render_template("poll.html", data = poll_data)
poll_data = {
   'question' : 'What is your favorite color?',
   'fields'   : ['Red', 'Blue', 'Orange', 'Green', 'Purple']
}
filename = '/tmp/data.txt'

@app.route('/poll')
def poll():
    vote = request.args.get('field')
    save = open(filename, 'a')
    save.write(vote + '\n')
    save.close()
    return render_template('thankyou.html', data=poll_data)

@app.route('/results')
def show_results():
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0

    f  = open(filename, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1

    return render_template('results.html', data=poll_data, votes=votes)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)