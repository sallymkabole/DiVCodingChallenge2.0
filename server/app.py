from flask import Flask, jsonify, request
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

@app.route('/tasks', methods=['GET','POST'])
def all_tasks():
    respose_object={'status':'success'}
    if request.method =='POST':
        post_data = request.get_json()
        TASKS.append({
            'title':post_data.get('title'),
            'severity':post_data.get('severity'),
            'start':post_data.get('start'),
            'end':post_data.get('end'),
            'done':post_data.get('done'),
        })
    else:
        respose_object['tasks'] =TASKS
    return jsonify(respose_object)


if __name__ == '__main__':
    app.run()