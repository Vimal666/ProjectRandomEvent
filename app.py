from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/create_event', methods=['POST'])
def receive_data():
    # Get JSON data from the request
    data = request.get_json()
    
    # Print the received data to the console
    print("Received data:", data)
    
    # Return a response


    response=  {
                    "code": 200,
                    "Data": data,
                    "status": {
                        "processed_at": datetime.now().strftime("%d-%B-%Y %X"),
                        "statusMessage": "Even Created successfully"
                    }
                }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
