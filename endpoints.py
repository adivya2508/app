import logging
from flask_pymongo import pymongo
from flask import jsonify, request
con_string = "mongodb+srv://DIVYA:<divyadivya>@cluster0.lbuoiji.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_string)
db=client.get_database('demodb')
user_collection = pymongo.collection.Collection(db,'demo')
print("Mongodb connected successfully")
def project_api_routes(endpoints):
    @endpoints.route('/hello',methods=['GET'])
    def hello():
        res='hello'
        print("hello")
        return res
    
    @endpoints.route('/register-user',methods=['POST'])
    def register_user():
        resp={}
        try:
            req_body = request.json
            user_collection.insert_one(req_body)
            print("User data stored successfully in Database")
            status = {
                "StatusCode":"200",
                "statusMessage":"User data stored successfully in Database"
                
            }
        except Exception as e:
            print(e)
            status={
                "StatusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"]=status
        return resp