import logging
from flask_pymongo import pymongo
from flask import jsonify, request
con_string = "mongodb+srv://DIVYA:divyadivya@cluster0.lbuoiji.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_string)
db = client.get_database('demodb')
user_collection = pymongo.collection.Collection(db, 'demo')
print("mongodb connected successfully")
def project_api_routes(endpoints):
    @endpoints.route('/hello',methods=['GET'])
    def hello():
        res = 'hello'
        print("hello")
        return res
    @endpoints.route('/reg',methods=['POST'])
    def reg():
        resp={}
        try:
            req_body = request.json
            user_collection.insert_one(req_body)
            print("User Data Stored Successfully in the Database.")
            status = {
                "statusCode":"200",
                "statusMessage":"UserData stored into the Database successfully"}
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)}
        resp["status"] = status
        return resp
    @endpoints.route('/read',methods=['GET'])
    def read():
        resp = {}
        try:
            users = user_collection.find({})
            print(users)
            users = list(users)
            print("User Data Retrived Successfully from the Database.")
            status = {
                "statusCode":"200",
                "statusMessage":"User Data Retrived Successfully from the Database."}
            output = [{'Name' : user['name'], 'Email' : user['email']} for user in users] #List comprehension
            resp['data']=output
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)}
        resp["status"] = status
        return resp
    @endpoints.route('/upd',methods=['PUT'])
    def upd():
        resp={}
        try:
            req_body = request.json
            user_collection.update_one({"id":req_body['id']}, {"$set": req_body['updated_user_body']})
            print("User Data Updated Successfully in the Database.")
            status = {
                "statusCode":"200",
                "statusMessage":"User Data Updated Successfully in the Database."}
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)}
        resp["status"] = status
        return resp
    @endpoints.route('/delete_user',methods=['DELETE'])
    def delete():
        resp = {}
        try:
            delete_id = request.args.get('detele_id')
            user_collection.delete_one({"id":delete_id})
            status = {
                "statusCode":"200",
                "statusMessage":"User data deleted Successfully from the Database."}
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)}
        resp["status"] = status
        return resp
    return endpoints
    
   
    