from fastapi import FastAPI, HTTPException
from module import Users

app = FastAPI()

users = [Users(id=1234,name='luffy',email='luffy@gmail.com',password='luffy123'),
        Users(id=12345,name='zoro',email='zoro@gmail.com',password='zoro123'),
        Users(id=123456,name='sanji',email='sanji@gmail.com',password='sanji123')]

@app.get('/')
def view_user():
    return users

@app.post('/')
def add_user(add_user:Users):
    for u in users:
        if add_user.id == u.id:
            raise HTTPException(status_code=400,detail='ID already exist')
        if add_user.name == u.name:
            raise HTTPException(status_code=400, detail='name already exist')
        users.append(add_user)
        return {'message':'Added successfully'}

@app.post('/update_user')
def update_user(u_id:int,user_update:Users):
        for u in range(len(users)):
            if users[u].id == u_id:
                users[u] = user_update
                return {'message': 'Update successfully'}
        raise HTTPException(status_code=400,detail='Not found')

@app.post('/delete_user')
def delete_user(u_id:int,user_delete:Users):
    for u in range(len(users)):
        if users[u].id == u_id:
            users[u] = user_delete
            del users[u]
            return {'message':'Deleted successfully'}
    raise HTTPException(status_code=400,detail='User to delete not found')
