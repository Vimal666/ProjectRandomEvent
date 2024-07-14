from flask import Flask, request, jsonify
from events import all_events
app = Flask(__name__)

#to create event
@app.route('/create_event', methods=['POST'])
def receive_data():
    # Get JSON data from the request
    data = request.get_json()
    
    responses=all_events.create_event(data)
    
    return jsonify(responses)


#to find an event
@app.route('/find_event', methods=['GET'])
def find_data():
    # Get JSON data from the request
    categories = request.get_json()
    if "categories" in categories:
        categories=categories["categories"]
    else:
        return {"code" : "400",
                "message": "invalid parameter"}
    print("dataaaaaaaaaaaa",categories)
    final_res=all_events.find_events(categories)
    print("lennnnnnnnnnnnnnnn,",len(final_res))
    # Add total count as a new dictionary in the list
    total_requests = {'total': len(final_res)}
    
    different_count={}
    for i in final_res:
        count=0
        for j in final_res:
            if j['Data']['event_category'] == i['Data']['event_category']:
                count+=1
        different_count[i['Data']['event_category']]=count
    #responses[{"total_count"}]=len(responses)
    print("finddddddddddddddddddddddddddddd", final_res)

    final_res.insert(0, total_requests)
    different_count = {'different_count': different_count}

    final_res.insert(1, different_count)

    
    return jsonify(final_res)

if __name__ == '__main__':
    app.run(debug=True)
