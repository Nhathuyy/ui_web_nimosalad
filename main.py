# app.py
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection details
mongo_uri = "mongodb+srv://huetravel:nhathuy2001@cluster0.xwhsaa4.mongodb.net/?retryWrites=true&w=majority"
db_name = "Nimo_game"
collection_name = "Top5Predictions"

@app.route('/')
def index():
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Retrieve the latest document from MongoDB
    latest_prediction = collection.find_one(sort=[('_id', -1)])

    if latest_prediction:
        round_number = latest_prediction.get('round_number', '')
        predicted_values = ', '.join(latest_prediction.get('predicted_values', []))
        predicted_values_1 = ', '.join(latest_prediction.get('predicted_values_1', []))
        top_5_results = latest_prediction.get('top_5_results', [])

        return render_template('index.html', round_number=round_number, predicted_values=predicted_values,
                               predicted_values_1=predicted_values_1, top_5_results=top_5_results)
    else:
        return "No predictions found in the database."

from flask import jsonify

@app.route('/api/predictions')
def get_latest_predictions():
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Retrieve the latest document from MongoDB
    latest_prediction = collection.find_one(sort=[('_id', -1)])

    if latest_prediction:
        round_number = latest_prediction.get('round_number', '')
        predicted_values = latest_prediction.get('predicted_values', [])
        predicted_values_1 = latest_prediction.get('predicted_values_1', [])
        top_5_results = latest_prediction.get('top_5_results', [])

        return jsonify({
            'round_number': round_number,
            'predicted_values': predicted_values,
            'predicted_values_1': predicted_values_1,
            'top_5_results': top_5_results
        })
    else:
        return jsonify({'error': 'No predictions found in the database'}), 404
if __name__ == '__main__':
    app.run(debug=True)