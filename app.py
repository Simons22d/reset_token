from flask import Flask
import time
import requests
import eventlet
import eventlet.wsgi
app = Flask(__name__)

def reset_ticket():
    from datetime import datetime
    time.sleep(3)
    this_time = datetime.now()
    if this_time:
        split_time = str(this_time)
        formatted_string = f"{split_time.split(' ')[0] } { split_time.split('.')[0]}"#%H:%M:%S
        if formatted_string == "2020-04-15 00:00"  or formatted_string == "2020-04-15 00:01" or formatted_string == "2020-04-15 00:02":
            requests.post("http://localhost:1000/reset/ticket/counter")
    print(this_time)
    # run a function to check time
    return True


while True :
    reset_ticket()


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 1000)), app)
