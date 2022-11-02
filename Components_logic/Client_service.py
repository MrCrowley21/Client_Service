from time import sleep
import random
import requests
import logging
from copy import copy
from threading import Thread, Lock

from config import *
from Components_logic.Individual_order import *
from Components_logic.Client import *

# initialize the logger mode
logging.basicConfig(level=logging.DEBUG)


class ClientService:
    def __init__(self):
        self.id_generator = 1
        self.lock = Lock()
        self.client_nr = 0

    def create_client(self):
        while True:
            sleep(random.randint(5, 20) * time_unit)
            client = Client(self.id_generator)
            self.id_generator += 1
            self.lock.acquire()
            self.client_nr += 1
            self.lock.release()
            Thread(target=client.make_an_order).start()
