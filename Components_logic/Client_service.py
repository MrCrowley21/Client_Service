from time import sleep
import random
import requests
import logging
from threading import Thread

from config import *

# initialize the logger mode
logging.basicConfig(level=logging.DEBUG)


class ClientService:
    def create_client(self):
        while True:
            sleep(random.randint(5, 15) * time_unit)
            Thread(target=self.request_menu).start()

    def request_menu(self):
        menu = requests.get(f'{food_ordering_container_url}menu').text
        logging.info(f'{menu}')
