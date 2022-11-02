import random
import requests
import time
from time import sleep
import logging
from threading import Thread, Barrier

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
        restaurant_data = requests.get(f'{food_ordering_url}menu').json()
        logging.info(f'Getting the menu from Food Ordering Service')
        return restaurant_data

    def generate_order(self, menu):
        orders = []
        total_items_nr = random.randint(1, 5)
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
                max_wait = 1.8 * max(
                    i['preparation-time'] for i in items)  # set the max waiting time for order receiving
                if max_wait < 18:
                    priority = 5
                elif max_wait < 23:
                    priority = 4
                elif max_wait < 34:
                    priority = 3
                elif max_wait < 45:
                    priority = 2
                else:
                    priority = 1
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

    def pick_up_order(self, barrier, address, order_id, wait_time):
        sleep(wait_time)
        response = requests.get(f'{address}v2/order/{order_id}').json()
        logging.info(f'22222222222 {response}')
        wait_time = response['estimated_waiting_time']
        while wait_time > 0:
            response = requests.get(f'{address}v2/order/{order_id}').json()
            wait_time = response['estimated_waiting_time']
            sleep((wait_time + wait_time * 0.15) * time_unit)
        barrier.wait()

    def wait_picking_up_order(self, orders):
        orders.sort(key=lambda x: x['estimated_waiting_time'])
        sleep_time = orders[0]['estimated_waiting_time']
        sleep_time = (sleep_time + sleep_time * 0.15) * time_unit
        barrier = Barrier(len(orders) + 1)
        for order in orders:
            t = Thread(target=self.pick_up_order, args=(barrier, order["restaurant_address"], order["order_id"], sleep_time))
            t.start()
            t.join()
        barrier.wait()
        del self

    def make_an_order(self):
        restaurant_data = self.request_menu()
        if restaurant_data['restaurants'] == 0:
            del self
        else:
            menu = restaurant_data['restaurants_data']
            self.generate_order(menu)
            logging.info(f'Client {self.client_id} generated a new order with the following structure:\n{self.__dict__}')
            response = requests.post(f'{food_ordering_url}order', json=self.__dict__).json()
            logging.info(f'The client {self.client_id} sent a the order to the Food Ordering Service')
            logging.info(f'Receiving response from the Food Ordering System\n{response}')
            self.wait_picking_up_order(response['orders'])
