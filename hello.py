
from flask import Flask,jsonify,request
app = Flask(__name__)


# jinja template
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/about',methods=['GET'])
def about():
    if(request.method=='GET'):
        data={
            "name":"Rahul",
            "age":21,
        }
        return jsonify(data)
app.run()