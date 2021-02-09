from flask import Flask
from flask import jsonify
from flask import request, render_template
import pandas as pd
import wikipedia
import time
import datetime


app = Flask(__name__)

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """
@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/bob')
def bob():
    val = {"value":"bob"}
    return jsonify(val)

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
    save = open(filename, 'wb')
    save.write(vote + '\n' )
    save.close()
    return render_template('thankyou.html', data=poll_data)

@app.route('/results')
def show_results():
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0

    f  = open(filename, 'wb')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1

    return render_template('results.html', data=poll_data, votes=votes)

# @app.route('/time_between')
# def time_between():
#     # dates to be comapred
#     date_now = datetime.datetime.now()
#     d = request.args.get('d', date_now)
#     d = datetime.datetime.strptime(d, "%d-%m-%Y %H:%M:%S")

#     # Get difference in units that can be understood easily
#     difference = d - date_now
#     duration_in_s = difference.total_seconds()

#     days    = divmod(duration_in_s, 86400)        
#     hours   = divmod(days[1], 3600)               
#     minutes = divmod(hours[1], 60)                
#     seconds = divmod(minutes[1], 1)  
#     return (
#         """<form action="" method="get">
#             Figure out how much time between two dates!
#             Enter your time and date: MM-DD-YYYY H:M:S <br><br>
#             Input: <input type="text" name="d">
#             <input type="submit" value="Calculate">
#         </form>"""
#     + f"Days: {days[0]}, Hours: {hours[0]}, Minutes: {minutes[0]}, Seconds: {seconds[0]}"
#     )

@app.route('/wikipedia/<company>')
def wikipedia_route(company):

    # Imports the Google Cloud client library
    from google.cloud import language
    result = wikipedia.summary(company, sentences=10)

    client = language.LanguageServiceClient()
    document = language.Document(
        content=result,
        type_=language.Document.Type.PLAIN_TEXT)
    encoding_type = language.EncodingType.UTF8
    entities = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type}).entities
    return str(entities)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)