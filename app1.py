from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
from analysis import analysistpt

# from flask_jwt import JWT, jwt_required
# from security import authenticate, identity

app = Flask(__name__)
# app.secret_key = 'arya'
api = Api(app)

# jwt = JWT(app, authenticate, identity) #/auth

# df = pd.read_csv('final_data.csv', index_col = 0)
# df = df.to_json(orient = 'index')
items = [

    {
        'name': 'arya',
        'price': 15.00
    },
    {
        'name': 'aditya',
        'price': 15.00
    }
]

class Tpt(Resource):
    def get(self):
        return({'trans': analysistpt()}), 200


class Item(Resource):
    # @jwt_required
    def get(self, name):
        item = list(filter(lambda x: x['name']==name, items))
        item = next(filter(lambda x: x['name']==name, items), None)
        # for item in items:
        #     if item['name'] == name:
        #         return item
        return({'item': item}), 200 if item  else 404

    def post(self, name):
        # items_data = request.get_json(force = True)
        #items_data = request.get_json(silent = True)
        if item == next(filter(lambda x: x['name']==name, items), None) is not None:
            return({'message': "An item with name '{}' already exisit".format(name)}, 400)

        items_data = request.get_json()
        item = {
        'name' : name,
        'price': items_data['price']
        }
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Tpt, '/trans')

app.run(port= 5000, debug = True)



# class Student(Resource):
#     def get(self, name):
#         return{'student': name}
#
# api.add_resource(Student, '/student/<string:name>')
