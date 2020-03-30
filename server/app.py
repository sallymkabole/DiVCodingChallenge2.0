from flask import Flask, jsonify
from flask_cors import CORS

TASKS = [
    {
        'title':'Draft Digital Compaign',
        'severity':'5',
        'start':'12/03/2020',
        'end':'22/03/2020',
        'done':True,
    },
     {
        'title':'User Reserch',
        'severity':'3',
        'start':'10/03/2020',
        'end':'12/03/2020',
        'done':False,
    }
]
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/tasks', methods=['GET'])
def all_tasks():
    return jsonify({
        'status':'success',
        'tasks':TASKS
    })


if __name__ == '__main__':
    app.run()