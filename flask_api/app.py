from flask import Flask,abort,jsonify,request
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
        temp_data = []
        # json_data()
        # new_data = [{'id':1,'name':'luffy','email':'luffy@gmail.com'},
        #             {'id':2,'name':'zoro','email':'zoro@gmail.com'},
        #             {'id':3,'name':'sanji','email':'sanji@gmail.com'}]
        with open(datas,'r') as f:
            temp_data = json.load(f)
        new_data = request.get_json()

        if any(new_data['id'] == temp['id'] for temp in temp_data):
            return jsonify({'message':'Already exist'})

        temp_data.append(new_data)
        with open(datas,'w') as f:
            json.dump(temp_data,f,indent=4)
        return jsonify({'message':'Successfully added'})

    except FileNotFoundError:
        abort(404,description='json not found')
@app.route('/updateinfo',methods=['POST','GET'])
def update_info():
    try:
        temp_data = []
        with open(datas,'r') as f:
            temp_data = json.load(f)
        # update_data = {'id':10,'name':'brook','email':'brook@gmail.com'}
        update_data = request.get_json()

        record = next((temp for temp in temp_data if update_data['id'] == temp['id']),None)

        if record is not None:
            record['name'] = update_data.get('name', record['name'])
            record['email'] = update_data.get('email', record['email'])

            with open(datas,'w') as f:
                json.dump(temp_data,f,indent=4)
            return jsonify({'message': 'Successfully updated'})

        return jsonify({'message': 'ID not found'}),404

    except FileNotFoundError:
        abort(404,description='json not found')
@app.route('/deleteinfo',methods=['POST'])
def delete_info():
    try:
        temp_data = []
        with open(datas,'r') as f:
            temp_data = json.load(f)

        # delete_data = {'id': 2, 'name': 'zoro', 'email': 'zoro@gmail.com'}
        delete_data = request.get_json()
        if_match = next(((n,temp) for n,temp in enumerate(temp_data) if delete_data['id'] == temp['id']),None)
        # for n,temp in enumerate(temp_data):
        if not if_match:
            return jsonify({'message':'Not found'})

        del temp_data[if_match[0]]
        with open(datas,'w') as f:
            json.dump(temp_data,f,indent=4)
        return jsonify({'message': 'Successfully deleted'})

    except FileNotFoundError:
        abort(404,description='json not found')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)