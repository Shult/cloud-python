# # Product Service
#
# # Import framework
# from flask import Flask
# from flask_restful import Resource, Api
#
# # Instantiate the app
# app = Flask(__name__)
# api = Api(app)
#
# class Product(Resource):
#     def get(self):
#         return {
#             'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs']
#         }
#
# # Create routes
# api.add_resource(Product, '/')
#
# # Run the application
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80, debug=True)
from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://mongodb:27017/")
db = client.myshop
collection = db.products

class Product(Resource):
    def get(self):
        products = collection.find({}, {'_id': 0, 'name': 1})
        return {'products': [product['name'] for product in products]}

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
