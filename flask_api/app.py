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

@app.route('/addinfo',methods=['POST'])
def add_info():
    try:
        json_data()
        new_data = [{'id':1,'name':'luffy','email':'luffy@gmail.com'},
                    {'id':2,'name':'zoro','email':'zoro@gmail.com'},
                    {'id':3,'name':'sanji','email':'sanji@gmail.com'}]
        with open(datas,'w') as f:
            json.dump(new_data,f,indent=4)
        return jsonify({'message':'Successfully added'})

    except FileNotFoundError:
        abort(404,description='json not found')
@app.route('/updateinfo',methods=['POST','GET'])
def update_info():
    try:
        data = json_data()
        new_data = {'id':8,'name':'jinbei','email':'luffy@gmail.com'}
        for d in data:
            if new_data['id'] == d['id']:
                return jsonify({'message': 'already exist'})
        data.append(new_data)
        with open(datas,'w') as f:
            json.dump(data,f,indent=4)
        return jsonify({'message': 'Successfully added'})

    except FileNotFoundError:
        abort(404,description='json not found')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)