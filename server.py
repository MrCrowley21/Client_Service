import logging
from threading import Thread
from flask import Flask, request, jsonify

# initialize the logger mode
logging.basicConfig(level=logging.DEBUG)

# initialize the server (app)
app = Flask(__name__)

# start the program execution
if __name__ == "__main__":
    # initialize server as a thread
    Thread(target=lambda: app.run(port=5003, host="0.0.0.0", debug=True, use_reloader=False)).start()
