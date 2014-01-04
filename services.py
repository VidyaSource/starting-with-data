from flask import Flask, Response
import json
import urllib2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Everything is running!'

@app.route('/projects/highpoverty/states')
def high_poverty_states():
    donors_choose_url = "http://api.donorschoose.org/common/json_feed.html?highLevelPoverty=true&APIKey=DONORSCHOOSE"
    response = urllib2.urlopen(donors_choose_url)
    json_response = json.load(response)
    states = set()
    for proposal in json_response["proposals"]:
        states.add(proposal["state"])

    return json.dumps(list(states))


if __name__ == '__main__':
    app.run()
