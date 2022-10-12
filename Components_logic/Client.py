import random
import requests
import time
import logging

from config import *
from Components_logic.Order import *
from Components_logic.Individual_order import *
from Components_logic.Client_service import *

# initialize the logger mode
logging.basicConfig(level=logging.DEBUG)


class Client:
    def __init__(self, client_id):
        self.client_id = client_id
        self.orders = []

    def request_menu(self):
        restaurant_data = requests.get(f'{food_ordering_container_url}menu').json()
        logging.info(f'Getting the menu from Food Ordering Service')
        return restaurant_data

    def generate_order(self, menu):
        orders = []
        total_items_nr = random.randint(1, 10)
        total_ordered = 0
        for restaurant in menu:
            if restaurant != menu[-1]:
                items_nr = random.randint(0, total_items_nr - total_ordered)
                total_ordered += items_nr
            else:
                items_nr = total_items_nr - total_ordered
            if items_nr > 0:
                items = random.choices(restaurant['menu'], k=items_nr)
                items_id = [i['id'] for i in items]
                if items_nr < 10:
                    priority = 5 - (items_nr // 2)  # set priority (by the number of orders)
                else:
                    priority = 1
                max_wait = 1.8 * max(i['preparation-time'] for i in items)  # set the max waiting time for order receiving
                orders.append(IndividualOrder(restaurant['restaurant_id'], items_id, priority, max_wait))
        creation_time = time.time()
        self.set_order_time(creation_time, orders)
        self.populate_order_list(orders)

    def set_order_time(self, creation_time, orders):
        for order in orders:
            order.created_time = creation_time

    def populate_order_list(self, orders):
        for order in orders:
            self.orders.append(order.__dict__)

    def put_an_order(self):
        restaurant_data = self.request_menu()
        menu = restaurant_data['restaurants_data']
        logging.info(f'{menu}')
        self.generate_order(menu)
        logging.info(f'The client {self.client_id} generated a new order')
        requests.post(f'{food_ordering_container_url}order', json=self.__dict__)
        logging.info(f'The client {self.client_id} sent a the order to the Food Ordering Service')
