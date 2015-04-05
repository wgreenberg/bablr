import json
from flask import Flask, request, Response, render_template

from app import bablr

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blab')
def blab():
    res = Response(mimetype='application/json')
    inputdata = request.args.get('input')
    if inputdata is None:
        res.status_code = 400
        return res

    out = {
        'input': inputdata,
        'message': bablr.lookup(inputdata)
    }
    res.data = json.dumps(out)
    return res

if __name__ == '__main__':
    app.run()
