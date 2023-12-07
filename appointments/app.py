from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from pymongo import MongoClient
app = Flask(__name__)

CORS(app)  # Enable CORS for your Flask app

client = MongoClient('mongodb://localhost:27017/') 
db = client['Appointment']
collection = db['appointments'] 
# hardappointments = [
#   { 'id': "1",'doctor': "1", 'date': "21 Nov 2023", 'rating':"Good"  },
#   { 'id': "2",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
#   { 'id': "3",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
#   { 'id': "4",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
#   { 'id': "5",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
# ]
# [
#   { "id": "1","doctor": "1", "date": "21 Nov 2023", "rating":"Good"  },
#   { "id": "2","doctor": "1", "date": "22 Nov 2023", "rating":"Bad"  },
#   { "id": "3","doctor": "2", "date": "22 Nov 2023", "rating":"Good"  },
#   { "id": "4","doctor": "1", "date": "22 Nov 2023", "rating":"Bad"  },
#   { "id": "5","doctor": "2", "date": "22 Nov 2023", "rating":"Good"  }
# ]
@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

# @app.route('/appointments', methods=["GET"])
# def getAppointments():
#   return jsonify(appointments)

@app.route('/appointments', methods=["GET"])
def getAppointments():
  appointments = list(collection.find({}, {'_id': 0}))
  # print ("hardappointments: ", hardappointments)
  # print("appointments: ", appointments)
  return jsonify(appointments)


# @app.route('/appointment/<id>', methods=["GET"])
# def getAppointment(id):
#   id = int(id) - 1
#   # return jsonify(appointments[id])
#   return jsonify({'id': appointments[id]['id'], 'doctor': appointments[id]['doctor'], 'date': appointments[id]['date'], 'rating': appointments[id]['rating']})

@app.route('/appointment/<id>', methods=["GET"])
def getAppointment(id):
    appointment = collection.find_one({'id': id}, {'_id': 0})  # Find appointment by ID
    if appointment:
        return jsonify(appointment)
    else:
        return jsonify({"message": "Appointment not found"}), 404

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=7070)