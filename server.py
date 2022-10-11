import logging
from threading import Thread
from flask import Flask, request, jsonify

from Components_logic.Client_service import *

# initialize the logger mode
logging.basicConfig(level=logging.DEBUG)

# initialize the server (app)
app = Flask(__name__)

# start the program execution
if __name__ == "__main__":
    # initialize server as a thread
    Thread(target=lambda: app.run(port=5003, host="0.0.0.0", debug=True, use_reloader=False)).start()
    client_service = ClientService()
    client_service.create_client()
