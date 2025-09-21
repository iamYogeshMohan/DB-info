from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    phone = request.form.get('phone')

    # Insert into MongoDB
    collection.insert_one({
        "name": name,
        "age": age,
        "phone": phone
    })

    return "<h2>Data submitted successfully!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
