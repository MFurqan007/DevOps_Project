from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from pymongo import MongoClient
app = Flask(__name__)

CORS(app)  # Enable CORS for your Flask app

client = MongoClient('mongodb://localhost:27017/') 
db = client['Doctor']
collection = db['doctors'] 

# doctors = [
#   { 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality':"DevOps"  },
#   { 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality':"Test"  }
# ]

@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

# @app.route('/doctors', methods=["GET"])
# def getDoctors():
#   return jsonify(doctors)
@app.route('/doctors', methods=["GET"])
def getDoctors():
  doctors = list(collection.find({}, {'_id': 0}))
  return jsonify(doctors)

# @app.route('/doctor/<id>', methods=["GET"])
# def getDoctor(id):
#   id = int(id) -1
#   # return jsonify({"id": doctors[id].id, "firstName": doctors[id].firstName, "lastName": doctors[id].lastName, "speciality": doctors[id].speciality}) -> This line of Code is Faulty
#   # return jsonify(doctors[id])  -> This is Solution 1 for the faulty line of code
#   # print({'id': doctors[id]['id'], 'firstName': doctors[id]['firstName'], 'lastName': doctors[id]['lastName'], 'speciality': doctors[id]['speciality']}) -> This is Solution 2 for the faulty line of code
#   return jsonify({'id': doctors[id]['id'], 'firstName': doctors[id]['firstName'], 'lastName': doctors[id]['lastName'], 'speciality': doctors[id]['speciality']})
@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
  doctor = collection.find_one({'id': id}, {'_id': 0})  # Find appointment by ID
  if doctor:
      return jsonify(doctor)
  else:
      return jsonify({"message": "Doctor not found"}), 404

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=9090)