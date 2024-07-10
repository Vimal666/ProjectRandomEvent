from flask import Flask, request, jsonify
from events import all_events
app = Flask(__name__)

@app.route('/create_event', methods=['POST'])
def receive_data():
    # Get JSON data from the request
    data = request.get_json()
    
    responses=all_events.create_event(data)
    
    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True)
