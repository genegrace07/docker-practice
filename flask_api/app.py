from flask import Flask,abort,jsonify
import json

app = Flask(__name__)
datas = 'data.json'

def json_data():
    with open(datas,'r') as f:
        read_data = json.load(f)
        return read_data

@app.route('/',methods=['GET'])
def view_data():
    try:
        view = json_data()
        return view
    except json.JSONDecodeError:
        abort(400,description='json not found')

@app.route('/addinfo',methods=['POST','GET'])
def add_info():
    try:
        json_data()
        new_data = {'id':1,'name':'luffy','email':'luffy@gmail.com'}
        with open(datas,'w') as f:
            json.dump(new_data,f,indent=4)
        return jsonify({'message':'Successfully added'})

    except FileNotFoundError:
        abort(404,description='json not found')

if __name__ == "__main__":
    app.run(debug=True)