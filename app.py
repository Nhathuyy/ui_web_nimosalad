from flask import Flask, render_template
from flask_socketio import SocketIO
from pymongo import MongoClient

app = Flask(__name__, template_folder="app")
socketio = SocketIO(app)

# MongoDB connection details
mongo_uri = "mongodb+srv://huetravel:nhathuy2001@cluster0.xwhsaa4.mongodb.net/?retryWrites=true&w=majority"
db_name = "Nimo_game"
collection_name = "Top5Predictions"

def get_latest_prediction():
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Retrieve the latest document from MongoDB
    latest_prediction = collection.find_one(sort=[('_id', -1)])

    return latest_prediction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predictions')
def get_latest_predictions():
    latest_prediction = get_latest_prediction()

    if latest_prediction:
        round_number = latest_prediction.get('round_number', '')
        predicted_values = latest_prediction.get('predicted_values', [])
        predicted_values_1 = latest_prediction.get('predicted_values_1', [])
        top_5_results = latest_prediction.get('top_5_results', [])

        return {
            'round_number': round_number,
            'predicted_values': predicted_values,
            'predicted_values_1': predicted_values_1,
            'top_5_results': top_5_results
        }
    else:
        return {'error': 'No predictions found in the database'}, 404

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    send_update()

def send_update():
    latest_prediction = get_latest_prediction()

    if latest_prediction:
        socketio.emit('prediction_update', {
            'round_number': latest_prediction.get('round_number', ''),
            'predicted_values': latest_prediction.get('predicted_values', []),
            'predicted_values_1': latest_prediction.get('predicted_values_1', []),
            'top_5_results': latest_prediction.get('top_5_results', [])
        })

if __name__ == '__main__':
    socketio.run(app, debug=True)
