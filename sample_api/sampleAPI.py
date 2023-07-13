#!/usr/bin/env python3
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
from random2 import randint

app=Flask(__name__)
api=Api(app)

class ToDoList(Resource):
    def get(self):
        data=pd.read_csv('todolist.csv')
        data=data.to_dict(orient='records')
        return {'data':data}, 200

class Numbers(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('number', type=int,required=True,location="args")
        args = parser.parse_args()
        
        data=pd.read_csv('numbers.csv')
        number=args['number']
        data2=data.query("number==@number")
        data2 = data2.reset_index(drop=True)
        if data2.shape[0] > 0 :
            idx=randint(0, data2.shape[0]-1)
            return {'data':data2['fact'][idx]}, 200
        else:
            return {'data':"No facts for that number. Please select a number between 1 and 10."},200

api.add_resource(ToDoList, '/todolist')
api.add_resource(Numbers, '/numbers')

if __name__=='__main__':
    app.run(host='0.0.0.0')