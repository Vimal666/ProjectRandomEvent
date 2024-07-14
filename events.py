from mongo import Mongo
from datetime import datetime

class all_events:

    def create_event(data):
        # Print the received data to the console
        print("Received data:", data)
        
        # Return a response
        reference_number=Mongo.find_latest_reference_number()
        reference_number=int(reference_number[0])
        new_reference_number= reference_number+1
        print("333333333333333333333", new_reference_number)


        response=  {
                        "code": 200,
                        "Data": data,
                        "reference_number": new_reference_number,
                        "status": {
                            "processed_at": datetime.now().strftime("%d-%B-%Y %X"),
                            "statusMessage": "Even Created successfully"
                        }
                    }
        responses=dict(response)
        print("4444444444444444444444444",responses)
        print("555555555555555555555555",type(responses))
        insert_update = Mongo.insert_one(response, "new_events")
        
        print("Successfully inserted into MongoDB")
        return responses
    
    def find_events(categories):

        response=Mongo.find_event_db(categories)
        print("event dindedddddddddddddddddddddddddd",response)
        return response