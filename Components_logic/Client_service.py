from time import sleep
import random
import requests
import logging
from copy import copy
from threading import Thread

from config import *
from Components_logic.Individual_order import *
from Components_logic.Client import *

# initialize the logger mode
logging.basicConfig(level=logging.DEBUG)


class ClientService:
    def __init__(self):
        self.id_generator = 1

    def create_client(self):
        while True:
            sleep(random.randint(5, 20) * time_unit)
            client = Client(self.id_generator)
            self.id_generator += 1
            Thread(target=client.put_an_order).start()

    # def request_menu(self):
    #     restaurant_data = requests.get(f'{food_ordering_container_url}menu').json()
    #     logging.info(f'Getting the menu from Dinning Hall')
    #     return restaurant_data
    #
    # def generate_order(self, menu):
    #     available_menu = []
    #     total_items_nr = random.randint(1, 10)
    #     total_ordered = 0
    #     for restaurant in menu:
    #         if restaurant != menu[-1]:
    #             items_nr = random.randint(0, total_items_nr - total_ordered)
    #             total_ordered += items_nr
    #         else:
    #             items_nr = total_items_nr - total_ordered
    #         items = random.choices(restaurant[menu], k=items_nr)
    #         items_id = [i['id'] for i in items]
    #         if items_nr < 10:
    #             priority = 5 - (items_nr // 2)  # set priority (by the number of orders)
    #         else:
    #             priority = 1
    #         max_wait = 1.8 * max(i['preparation-time'] for i in items)  # set the max waiting time for order receiving


    # def put_an_order(self):
    #     restaurant_data = self.request_menu()
    #     menu = restaurant_data['restaurant_data']
    #     self.generate_order(menu)
