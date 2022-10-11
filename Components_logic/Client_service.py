from time import sleep
import random


class ClientService:
    def create_client(self):
        while True:
            sleep(random.randint(5, 15))

    def request_menu(self):
        sleep(1)
